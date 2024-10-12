<ol>
<li>메인(마스터) 브렌치로 이동</li>
</ol>
<pre><code class="language-bash">git checkout main</code></pre>
<ol start="2">
<li>메인 브랜치에 폴더 생성</li>
</ol>
<pre><code class="language-bash">mkdir {directory_name}</code></pre>
<ol start="3">
<li>브랜츠 변경 없이 파일만 가져오기</li>
</ol>
<pre><code class="language-bash">git checkout {branch_name} -- .</code></pre>
<ol start="4">
<li>파일 가져와서 폴더에 넣기</li>
</ol>
<pre><code class="language-bash">setopt extended_glob # ^ 문법 허용을 위함
mv ^{폴더에 넣지 않을 파일} {dir_name}/</code></pre>
<p>파일을 옮기는 것은 현재 경로에 있는 모든 파일을 해당 디렉토리로 옮기기 때문에 폴더에 넣지 않을 파일을 잘 선정해 주어야 합니다.</p>
<pre><code class="language-bash">mv {옮길 폴더} {옮길 위치(폴더)}</code></pre>
<p>위처럼 한 개씩 이동시키실 수도 있습니다.</p>
<hr />
<h4 id="모든-브랜치-fetch-해오기">모든 브랜치 fetch 해오기</h4>
<pre><code class="language-bash">git branch -r \
  | grep -v '\-&gt;' \
  | sed &quot;s,\x1B\[[0-9;]*[a-zA-Z],,g&quot; \
  | while read remote; do \
      git branch --track &quot;${remote#origin/}&quot; &quot;$remote&quot;; \
    done
git fetch --all
git pull --all</code></pre>