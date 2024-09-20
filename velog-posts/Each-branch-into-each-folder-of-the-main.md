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
git mv ^{폴더에 넣지 않을 파일} {dir_name}/</code></pre>
<p>파일을 옮기는 것은 현재 경로에 있는 모든 파일을 해당 디렉토리로 옮기기 때문에 폴더에 넣지 않을 파일을 잘 선정해 주어야 합니다.</p>