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
<p>커밋을 세고 반영하는 커밋은 반영되지 않도록 필터 로직을 추가했다</p>
<pre><code class="language-yml">name: Update Commit Activity Badges

on:
  push:
    branches:
      - main
  schedule:
    - cron: '59 23 * * *'
  workflow_dispatch:

jobs:
  update-commit-badges:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout Repo
        uses: actions/checkout@v2
        with:
          ref: main
          persist-credentials: true
          fetch-depth: 0

      - name: Setup Git Config
        run: |
          git config --global user.email &quot;github-actions[bot]@github.com&quot;
          git config --global user.name &quot;github-actions[bot]&quot;

      - name: Count Total Commit Days (Exclude Badge Update Commits)
        id: total_commit_days
        run: |
          total_days=$(git log --format='%cd' --date=format:'%Y-%m-%d' --grep='badge' --invert-grep | sort -u | wc -l)
          echo &quot;total_commit_days=$total_days&quot; &gt;&gt; $GITHUB_ENV

      - name: Count Weekly Commit Days (Exclude Badge Update Commits)
        id: weekly_commit_days
        run: |
          weekly_days=$(git log --since='7 days ago' --format='%cd' --date=format:'%Y-%m-%d' --grep='badge' --invert-grep | sort -u | wc -l)
          echo &quot;weekly_commit_days=$weekly_days&quot; &gt;&gt; $GITHUB_ENV


      - name: Create Badges
        run: |
          total_badge_url=&quot;https://img.shields.io/badge/total_commit_days-${{ env.total_commit_days }}-blue?cache=$(date +%s)&quot;
          weekly_badge_url=&quot;https://img.shields.io/badge/weekly_commit_days-${{ env.weekly_commit_days }}-green?cache=$(date +%s)&quot;
          echo &quot;![Total Commit Days]($total_badge_url)&quot; &gt; total_commit_badge.md
          echo &quot;![Weekly Commit Days]($weekly_badge_url)&quot; &gt; weekly_commit_badge.md

      - name: Update README with Badges at Top
        run: |
          # Safely remove existing badge lines
          sed -i '/Total Commit Days/d' README.md || echo &quot;No Total Commit Days badge found to remove&quot;
          sed -i '/Weekly Commit Days/d' README.md || echo &quot;No Weekly Commit Days badge found to remove&quot;

          # Combine badges and the rest of the README
          cat total_commit_badge.md weekly_commit_badge.md README.md &gt; temp_readme.md
          mv temp_readme.md README.md

      - name: Stash Changes (if any) before Pull
        run: |
          git add .
          git stash push -m &quot;temp-stash-for-pull&quot; || echo &quot;Nothing to stash&quot;

      - name: Pull Latest Changes
        run: |
          git pull origin main --rebase || echo &quot;Rebase failed, attempting to continue&quot;

      - name: Apply Stash (if any)
        run: |
          git stash pop || echo &quot;No stash to apply&quot;

      - name: Commit Changes with Identifier
        run: |
          git add README.md
          git commit -m &quot;Update commit days badges [badge-update]&quot; || echo &quot;No changes to commit&quot;

      - name: Fetch Latest Changes Before Pushing
        run: |
          git fetch origin main
          git rebase origin/main || echo &quot;Rebase failed, attempting to resolve automatically&quot;
          git rebase --continue || echo &quot;No rebase to continue&quot;

      - name: Push Changes
        env:
          GH_PAT: ${{ secrets.GH_PAT }}
        run: |
          git push https://x-access-token:${GH_PAT}@github.com/TIL-challenge/becooq81.git || echo &quot;Push failed, trying to resolve&quot;
</code></pre>