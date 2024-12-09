<h1 id="jwt">JWT</h1>
<p>HTTP는 각 요청에 대해 매번 연결을 생성하고 끊는 비연결성, 그리고 요청에 대한 상태를 저장하지 않는 무상태성이라는 특징을 가진다. 불필요한 자원 낭비를 줄일 수 있는 장점이다. </p>
<p>하지만 서버는 클라이언트를 식별하지 못한다는 단점도 존재한다. 이번 요청으로 로그인에 성공해도, 상태를 저장하지 않기 때문에 이 클라이언트가 로그인했음을 기억하지 않는다. </p>
<h3 id="쿠키와-세션">쿠키와 세션</h3>
<p>이러한 단점을 해결하기 위해 쿠키와 세션을 사용한다. 쿠키는 클라이언트가 어떤 웹사이트를 방문할 경우, 그 사이트의 서버에 의해 클라이언트의 브라우저에 저장되는 key-value 형태의 정보 파일을 말한다. </p>
<p>이 쿠키를 통해 로그인 상태를 유지시킬 수 있지만, 쿠키는 브라우저에 저장되어 보안이 약하기 때문에 유출 및 조작 당할 위험이 존재한다. </p>
<p>세션은 정보를 브라우저가 아닌 서버 측에 저장하기 때문에 보안이 더 좋다. 인증 정보는 서버에 저장하고, 클라이언트 식별자인 <code>JSESSIONID</code>를 쿠키에 담아, 클라이언트는 요청을 보낼 때마다 <code>JSESSIONID</code> 쿠키를 보내면 서버가 유효성을 판단해 클라이언트를 식별한다. </p>
<p>그럼에도 해커가 <code>JSESSIONID</code> 쿠키를 탈취하면 클라이언트인 척 위장이 가능하고, 서버에 부하가 갈 수 있다는 단점이 존재한다. </p>
<h2 id="jwt-기반-인증">JWT 기반 인증</h2>
<p>JWT(JSON Web Token)은 인증에 필요한 정보를 암호화시킨 토큰을 의미한다. 쿠키/세션 방식과 유사하게 JWT 토큰(Access Token)을 HTTP 헤더에 실어 서버가 클라이언트를 식별한다. </p>
<h3 id="jwt의-구조">JWT의 구조</h3>
<p>JWT는 .을 구분자로 세 개의 문자열로 나뉜다. </p>
<ol>
<li><strong>Header</strong>: <code>alg</code>와 <code>typ</code>으로 각각 암호화할 해싱 알고리즘과 토큰의 타입을 지정한다</li>
</ol>
<pre><code>{
    &quot;alg&quot;: &quot;HS256&quot;,
    &quot;typ&quot;: &quot;JWT&quot;
}</code></pre><ol start="2">
<li><strong>Payload</strong>: 토큰에 담을 정보를 갖는다. 주로 클라이언트의 고유 ID 값 및 유효기간 등을 포함한다. </li>
</ol>
<p>key-value 형식으로, 한 쌍의 정보를 <strong>Claim</strong>이라 부른다</p>
<pre><code>{
    &quot;sub&quot;: &quot;12345812&quot;,
    &quot;name&quot;: &quot;Hong Gildong&quot;,
    &quot;iat&quot;: 2385123
}</code></pre><ol start="3">
<li><strong>Signature</strong>: 인코딩된 헤더와 페이로드를 더한 뒤 비밀키로 해싱하여 만든다.</li>
</ol>
<pre><code>HMACSHA256(
    base64URLEncode(header) + &quot;.&quot; + base64URLEncode(payload), {256-bit-secret}
)</code></pre><p>헤더와 페이로드는 단순히 인코딩된 값이기 때문에 제3자가 복호화 또는 조작할 수 있지만, Signature는 서버 측에서 관리하는 비밀키가 유출되지 않는 이상 복호화 할 수 없다. 따라서 Signature는 토큰의 위변조 여부를 확인하는데 사용된다. </p>
<h3 id="jwt의-인증-과정">JWT의 인증 과정</h3>
<ol>
<li>클라이언트가 로그인 요청을 보낸다</li>
<li>서버는 클라이언트의 요청과 데이터베이스에 저장된 사용자 정보를 비교해서 유효성을 확인한다</li>
<li>검증에 성공하면, 서버는 클라이언트의 고유 ID 등의 정보를 Payload에 담아 JWT를 생성한다.</li>
<li>서버는 발급한 JWT를 클라이언트에 전달하고, 클라이언트는 이 토큰을 저장한다.</li>
<li>클라이언트는 이후 서버에 요청할 때마다 토큰을 요청 헤더 <code>Authorization</code>에 포함시켜 함께 전달한다</li>
<li>서버는 요청을 받으면 토큰의 Signature를 비밀키로 복호환 다음, 위변조 여부 및 유효 기간 등을 확인한다</li>
<li>유효한 토큰이면 서버는 요청에 응답한다.</li>
</ol>
<h3 id="jwt의-장점">JWT의 장점</h3>
<ul>
<li>Header와 Payload로 Signature를 생성하므로 데이터 위변조를 막을 수 있다</li>
<li>인증 정보에 대한 별도의 저장소를 사용하지 않는다 <ul>
<li>JWT는 토큰에 대한 정보, 토큰 검증을 증명하는 서명 등 필요한 정보를 지니기 때문에 저장소를 필요로 하지 않는다</li>
<li>클라이언트 인증 정보를 저장하는 세션에 비해 장점이다</li>
</ul>
</li>
</ul>
<h3 id="jwt의-단점">JWT의 단점</h3>
<ul>
<li>토큰의 길이가 길어서 인증 요청이 많아지면 네트워크 부하가 존재한다</li>
<li>Pyaload 자체는 암호화되지 않기 때문에 유저의 중요한 정보는 담을 수 없다</li>
<li>토큰이 탈취 당하면 처리가 까다롭다</li>
</ul>
<h3 id="토큰을-탈취-당하면">토큰을 탈취 당하면?</h3>
<p>Access Token과 함께 Refresh Token을 발급한다. Access Token을 탈취 당하면 기존 Access Token을 무효화 시킨 다음, 사용자는 다시 로그인해서 Access Token를 새로 발급 받는다. </p>
<p>하지만 서버는 Refresh Token을 별도의 저장소에 저장해야 하기 때문에 저장소가 필요없는 JWT의 장점을 완전히 누릴 수는 없다. 저장소에 저장한다는 건 처리하기 위해 I/O 작업을 수반한다는 의미기도 하다. </p>
<p>이 Refresh Token까지 탈취 당하면 안타깝다..</p>
<hr />
<p>참고:</p>
<p><a href="https://tecoble.techcourse.co.kr/post/2021-05-22-cookie-session-jwt/">https://tecoble.techcourse.co.kr/post/2021-05-22-cookie-session-jwt/</a></p>