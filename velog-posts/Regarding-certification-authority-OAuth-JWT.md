<h1 id="인증authentication과-인가authorization">인증(Authentication)과 인가(Authorization)</h1>
<p>인증은 사용자가 누구인지 확인한다. 인가는 사용자의 접근 권한을 확인한다.</p>
<p>(예) 공항에서 여권을 보여주어 나를 인증할 수 있고, 탑승 게이트에서는 내 탑승권을 보여서 내 권한을 입증해야 탑승을 인가 받을 수 있다.</p>
<p><img alt="" src="https://velog.velcdn.com/images/becooq81/post/4a9bb664-5083-4b57-a71c-76ca9b33a72d/image.png" /></p>
<h1 id="oauth">OAuth</h1>
<p>OAuth는 인터넷 사용자들이 비밀 번호를 제공하지 않고, 다른 웹사이트 상의 자신의 정보에 대해 접근 권한을 부여할 수 있는 공통적인 수단으로서 사용되는, 접근 위임을 위한 개방형 표준이다. (위키백과)</p>
<p>(예) 외부 어플리케이션은 사용자 인증을 위해 카카오톡, Google 등의 사용자 인증 방식을 사용한다. 이 때 해당 외부 애플리케이션은 OAuth를 바탕으로 카카오톡, Google의 특정 자원을 접근 및 사용할 수 있는 권한을 인가 받는다</p>
<h2 id="oauth의-구성-요소">OAuth의 구성 요소</h2>
<ul>
<li><strong>Resource Server</strong>: 클라이언트가 제어하고자 하는 자원을 보유하고 있는 서버<ul>
<li>(예) 구글, 카카오톡 등</li>
</ul>
</li>
<li><strong>Resource Owner</strong>: 자원의 소유자<ul>
<li>클라이언트가 제공하는 서비스를 통해 로그인하는 실제 유저</li>
</ul>
</li>
<li><strong>Client</strong>: Resource Server에 접속하여 정보를 가져오고자 하는 클라이언트 (애플리케이션)</li>
</ul>
<h2 id="oauth의-동작-과정">OAuth의 동작 과정</h2>
<p>GitHub 계정으로 웹 애플리케이션에 로그인하고, GitHub에서 제공하는 여러 API 기능을 외부 애플리케이션에서 사용하는 동작 과정에 대해 알아본다</p>
<h3 id="1-클라이언트외부-애플리케이션-등록">1. 클라이언트(외부 애플리케이션) 등록</h3>
<p>클라이언트가 Resource Server를 이용하기 위해서는 자신의 서비스를 등록해서 사전 승인을 받아야 한다</p>
<p>GitHub의 경우에는 등록된 서비스에 다음과 같은 정보를 부여한다</p>
<ol>
<li>Client ID: 클라이언트 애플리케이션을 구별하는 식별자</li>
<li>Client Secret: Client ID에 대한 비밀키 (노출 금지)</li>
<li>Authorized redirect URL: Authorization Code를 전달받을 리다이렉트 주소</li>
</ol>
<p>외부 서비스를 통해 인증을 마치면 애플리케이션은 명시된 주소로 사용자를 리다이렉트 시킨다. 이 때 Query String으로 특별한 코드가 전달되는데, 애플리케이션은 해당 코드, Client ID, Client Secret을 Resource Server에 보내서 Resource Server의 자원을 사용할 수 있는 Access Token을 발급받는다.</p>
<h3 id="2-resource-owner의-승인">2. Resource Owner의 승인</h3>
<p>GitHub 소셜 로그인을 위해서는 다음과 같은 파라미터들이 요구된다</p>
<pre><code>GET https://github.com/login/oauth/authorize?client_id={client_id}&amp;redirect_uri={redirect_uri}?scope={scope}</code></pre><ul>
<li><strong>scope</strong>: 클라이언트가 Resource Server로부터 인가받을 권한의 범위</li>
</ul>
<p>Resource Owner가 Resource Server에 접속하여 로그인을 완료하면, Resource Server는 Query String으로 받은 파라미터들로 클라이언트를 검사한다</p>
<ul>
<li>파라미터로 받은 Client ID와 동일한 ID 값이 존재하는지 (사전등록된 애플리케이션인지)</li>
<li>해당 Client ID에 해당하는 Redirect URL이 파라미터로 전달된 Redirect URL와 같은지</li>
</ul>
<p>검증에 성공하면 Resource Server는 Resource Owner에게 명시한 scope에 대한 권한을 애플리케이션에 정말 부여할 것인지 질의한다. Resource Owner가 허용하면 Resource Server에게 Client의 접근을 승인하게 된다</p>
<h3 id="3-resource-server의-승인">3. Resource Server의 승인</h3>
<p>Resource Owner가 승인한 경우, Resource Server는 클라이언트를 명시된 Redirect URL로 리다이렉트 시킨다. Resource Server는 클라이언트가 자신의 자원을 사용할 수 있는 Access Token을 발급하기 전에, 임시 암호인 Authorization Code를 함께 발급한다.</p>
<p>클라이언트는 Query String으로 이 코드를 받고, (주로) DTO에 Client ID, Client Secrety Key와 함께 담아 Resource Server에 전달한다. Resource Server는 유효한 요청인지 검증한 다음 Access Token을 발급한다.</p>
<p>클라이언트는 해당 토큰을 서버에 저장해두고, Resource Server의 자원을 사용하기 위한 API 호출시 해당 토큰을 헤더에 담아 보낸다.</p>
<h3 id="4-api-호출">4. API 호출</h3>
<p>클라이언트는 Access Token을 헤더에 담아 GitHub API를 호출한다.</p>
<h3 id="5-refresh-token">5. Refresh Token</h3>
<p>Access Token에는 만료 기간이 있어서 만료된 토큰으로 API를 요청하면 401 Unauthorized 에러가 발생한다. Access Token이 만료될 때마다 서비스 이용자가 재로그인하는 것은 번거롭기 때문에 주로 Resource Server는 Access Token을 발급할 당시 Refresh Token을 함께 발급한다. </p>
<p>클라이언트는 두 토큰을 모두 저장한다. API를 호출할 때는 Access Token을 사용하고, Access Token이 만료되면 저장해둔 Refresh Token을 보내서 새로운 Access Token을 발급받는다.</p>
<hr />
<p>참고:</p>
<ul>
<li><a href="https://auth0.com/docs/get-started/identity-fundamentals/authentication-and-authorization">https://auth0.com/docs/get-started/identity-fundamentals/authentication-and-authorization</a></li>
<li><a href="https://tecoble.techcourse.co.kr/post/2021-07-10-understanding-oauth/">https://tecoble.techcourse.co.kr/post/2021-07-10-understanding-oauth/</a></li>
</ul>