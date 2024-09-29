<h1 id="문제">문제</h1>
<p>LeetHub은 기본적으로 레포지토리 root 기준으로 각 문제에 대한 폴더를 만들어서 업로드된다. 나는 이 LeetHub 결과를 폴더 하나로 모아두고 싶었다.</p>
<h1 id="해결-방안">해결 방안</h1>
<h2 id="1-leethub-레포지토리를-포크한다">1. LeetHub 레포지토리를 포크한다</h2>
<p>가장 최근 버전인 v3를 사용했다. v2는 폴더 구조 등이 달라 적용이 더 까다로운 것 같다</p>
<p>아래 깃허브 레포지토를 포크하면 된다.</p>
<p><a href="https://github.com/raphaelheinz/LeetHub-3.0">https://github.com/raphaelheinz/LeetHub-3.0</a></p>
<h2 id="2-포크한-레포를-로컬로-클론한다">2. 포크한 레포를 로컬로 클론한다</h2>
<pre><code class="language-bash">git clone https://github.com/{본인 깃허브 아이디}/LeetHub-3.0.git</code></pre>
<h2 id="3-프로젝트를-열어-scriptsleetcodejs-를-수정한다">3. 프로젝트를 열어 /scripts/leetcode.js 를 수정한다</h2>
<p><code>ctrl+F</code>로 <code>const URL</code>을 검색한 다음, URL 값의 <code>/contents/</code> 다음에 폴더 이름을 적는다. 총 2개의 <code>const URL</code>이 존재한다.</p>
<p><img alt="" src="https://velog.velcdn.com/images/becooq81/post/43fd9255-e695-4002-86e8-b37253cac2e8/image.png" /></p>
<p>나는 폴더 이름을 LeetCode로 설정했다.</p>
<h2 id="4-크롬-확장-프로그램에-업로드한다">4. 크롬 확장 프로그램에 업로드한다.</h2>
<p>chrome://extensions/</p>
<p>주소 창에 위 값을 입력하면 크롬의 확장 프로그램 관리 페이지로 이동한다.</p>
<p><img alt="" src="https://velog.velcdn.com/images/becooq81/post/e0dbffb9-b6df-4e4a-a794-b7cf5560f6a9/image.png" /></p>
<p>우측 상단에 개발자 모드를 활성화한다.</p>
<p>압축 해제된 프로그램을 업로드합니다 (Load unpacked) 버튼을 클릭해서 로컬의 LeetHub-3.0을 업로드한다</p>
<h2 id="5-맘껏-리트코드를-푼다-자동으로-업로드된다">5. 맘껏 리트코드를 푼다. 자동으로 업로드된다.</h2>
<hr />
<p>참고:
<a href="https://youngju-js.tistory.com/48">https://youngju-js.tistory.com/48</a></p>