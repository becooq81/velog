<h1 id="1-til을-할-레포지토리를-설정한다">1. TIL을 할 레포지토리를 설정한다</h1>
<h2 id="1-1-github-action-봇에-해당-레포지토리-쓰기-작업-권한을-부여한다">1-1. GitHub Action 봇에 해당 레포지토리 쓰기 작업 권한을 부여한다</h2>
<p>레포지토리의 <code>Settings</code> &gt; <code>Actions</code> &gt; <code>General</code> &gt; <code>Workflow Permissions</code> &gt; <code>Read and Write permissions</code> 선택</p>
<h2 id="1-2-personal-access-token-pat를-생성한다">1-2. Personal Access Token (PAT)를 생성한다</h2>
<p><code>GitHub</code> &gt; <code>Settings</code> &gt; <code>Developer Settings</code> &gt; <code>Personal access Tokens</code> &gt; <code>Generate new token</code></p>
<ul>
<li>이 토큰에 쓰기 권한을 허용해야 한다</li>
<li>토큰을 복사한다</li>
</ul>
<h2 id="1-3-pat를-레포지토리-시크릿에-추가한다">1-3. PAT를 레포지토리 시크릿에 추가한다</h2>
<p>TIL할 레포지토리의 <code>Settings</code> &gt; <code>Secrets and Variables</code> &gt; <code>Actions</code> 에서 <code>GH_PAT</code>라는 이름의 시크릿을 생성하고, 값에 복사해둔 토큰을 붙여넣는다</p>
<h1 id="2-github-workflow를-추가한다">2. GitHub Workflow를 추가한다</h1>
<p><code>.github/workflows/update_commit.yml</code>을 생성하고 다음을 복사한 후, github url을 적절하게 넣는다</p>
<pre><code class="language-yml">name: Update Commit Activity Badges

on:
  push:
    branches:
      - main
  schedule:
    - cron: '0 0 * * 0'  # 매주 일요일에 자동 런한다
  workflow_dispatch:  # 매뉴얼로 런할 수 있음

jobs:
  update-commit-badges:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout Repo
        uses: actions/checkout@v2
        with:
          ref: main  
          persist-credentials: true  
          fetch-depth: 0 # 모든 브랜치 및 태그에 대해 모든 커밋 로그를 확인한다
      - name: Setup Git Config
        run: |
          git config --global user.email &quot;github-actions[bot]@github.com&quot;
          git config --global user.name &quot;github-actions[bot]&quot;

      - name: Count Total Commit Days
        id: total_commit_days
        run: |
          # 전체 커밋 로그의 커밋 날짜를 출력한다

          echo &quot;All unique commit dates in the entire history:&quot;
          git log --format='%cd' --date=format:'%Y-%m-%d' | sort -u

          # 전체 커밋 로그의 유니크 날짜 수를 저장한다

          total_days=$(git log --format='%cd' --date=format:'%Y-%m-%d' | sort -u | wc -l)
          echo &quot;Total commit days found: $total_days&quot;
          echo &quot;total_commit_days=$total_days&quot; &gt;&gt; $GITHUB_ENV

      - name: Count Weekly Commit Days
        id: weekly_commit_days
        run: |
          # 지난 7일 중 커밋 로그에 존재하는 유니크 날짜를 저장한다

          echo &quot;Unique commit dates in the last 7 days:&quot;
          git log --since='7 days ago' --format='%cd' --date=format:'%Y-%m-%d' | sort -u

          # 지난 7일 중 커밋 로그에 존재하는 유니크 날짜의 수를 저장한다

          weekly_days=$(git log --since='7 days ago' --format='%cd' --date=format:'%Y-%m-%d' | sort -u | wc -l)
          echo &quot;Weekly commit days found: $weekly_days&quot;
          echo &quot;weekly_commit_days=$weekly_days&quot; &gt;&gt; $GITHUB_ENV

      - name: Create Badges
        run: |
          # cache-busting 인자로 리프레시를 강제하는 뱃지 URL를 생성한다

          total_badge_url=&quot;https://img.shields.io/badge/total_commit_days-${{ env.total_commit_days }}-blue?cache=$(date +%s)&quot;
          weekly_badge_url=&quot;https://img.shields.io/badge/weekly_commit_days-${{ env.weekly_commit_days }}-green?cache=$(date +%s)&quot;
          echo &quot;Total Badge URL: $total_badge_url&quot;
          echo &quot;Weekly Badge URL: $weekly_badge_url&quot;
          echo &quot;![Total Commit Days]($total_badge_url)&quot; &gt; total_commit_badge.md
          echo &quot;![Weekly Commit Days]($weekly_badge_url)&quot; &gt; weekly_commit_badge.md

      - name: Update README with Badges at Top
        run: |
          # 이미 뱃지가 있다면 없애고 리드미 맨 앞에 뱃지를 추가한다

          sed -i '/Total Commit Days/d' README.md
          sed -i '/Weekly Commit Days/d' README.md
          cat total_commit_badge.md weekly_commit_badge.md README.md &gt; temp_readme.md
          mv temp_readme.md README.md  # Replace the old README with the updated one

      - name: Commit Changes
        run: |
          git add README.md
          git status  
          git commit -m &quot;Update commit days badges&quot;

      - name: Push Changes
        env:
          GH_PAT: ${{ secrets.GH_PAT }}  # Ensure this token has push permissions
        run: |
          git push https://x-access-token:${GH_PAT}@github.com/{username}/{repository}.git</code></pre>