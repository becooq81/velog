<h1 id="web-server">Web Server</h1>
<p>웹서버는 웹사이트의 코드와 데이터를 호스팅하는 기술이다. 블로그, 헤더 이미지 등 정적인 콘텐츠를 호스팅한다.</p>
<p>브라우저에 입력하는 URL이 곧 이 웹서버의 주소 식별자고, 이 URL를 통해 브라우저는 웹서버와 통신한다.</p>
<ol>
<li>브라우저는 URL을 사용해 서버의 IP 주소를 찾는다</li>
<li>브라우저가 이 IP 주소에 HTTP 요청을 보낸다</li>
<li>웹서버가 데이터베이스 서버와 통신하여 해당 정보를 가져온다</li>
<li>웹서버가 브라우저에 이 정적 콘텐츠로 응답한다</li>
<li>브라우저가 정적 콘텐츠를 렌더링한다</li>
</ol>
<h1 id="web-application-server">Web Application Server</h1>
<p>웹 애플리케이션 서버는 동적 콘텐츠 생성, 애플리케이션 로직 등 다양한 방법으로 웹서버의 기능을 확장한다. </p>
<ol>
<li>브라우저가 URL을 사용해 서버의 IP 주소를 찾는다</li>
<li>브라우저가 이 IP 주소에 HTTP 요청을 보낸다</li>
<li>웹 서버는 이 요청을 웹 애플리케이션 서버로 전송한다</li>
<li>웹 애플리케이션 서버는 비즈니스 로직을 수행하고 다른 서버 등과 통신하여 작업을 수행한 다</li>
<li>웹 애플리케이션 서버는 새 HTML 페이지를 생성하여 웹서버에 응답으로 보낸다</li>
<li>웹서버는 브라우저에 이 응답을 보낸다</li>
<li>브라우저가 정보를 렌더링한다</li>
</ol>
<h1 id="ws-vs-was">WS vs. WAS</h1>
<h4 id="콘텐츠">콘텐츠</h4>
<p>WS와 WAS를 구분 짓는 가장 직관적인 차이는 각각 다루는 콘텐츠다.  WS는 주로 정적 콘텐츠만 처리하는 방면, WAS는 더 다양한 콘텐츠를 처리하는 편이다. </p>
<p>WS가 주로 처리하는 정적 콘텐츠는 별도의 처리 작업을 필요로 하지 않는 콘텐츠를 일컫는다. HTML 페이지, 이미지, 영상, PDF 등. </p>
<p>WAS가 주로 처리하는 동적 콘텐츠는 사용자의 상호작용에 따라 달라지는 콘텐츠다. 개인화된 UI, 데이터베이스 쿼리 결과 등</p>
<h4 id="프로토콜">프로토콜</h4>
<p>WS는 HTTP 프로토콜을 주로 사용하는데, 필요에 따라 FTP(File Transfer Protocol)이나 SMTP(Simple Mail Transfer Protocol) 등도 사용한다.</p>
<p>WAS는 RPC, RMI 등 더 다양한 프로토콜을 사용한다.</p>
<h4 id="멀티스레딩">멀티스레딩</h4>
<p>많은 웹 서버가 멀티스레딩을 지원하지 않는다. 웹서버가 처리하는 각 요청은 큐로 관리되고, 요청의 삽입과 삭제는 이벤트 루프로 관리된다. 성능 이슈를 보완하기 위해서 논블릭킹 I/O와 콜백이 사용된다.    </p>
<p>반면, 웹 애플리케이션 서버는 멀티스레딩 기반 병렬 처리로 서버의 가용성과 호율성을 향상시킨다. 즉, 여러 클라이언트의 요청을 동시에 처리할 수 있다. </p>
<h1 id="dmz-네트워크">DMZ 네트워크</h1>
<p>DMZ 네트워크는 내부 네트워크(LAN)를 외부 트래픽으로부터 안전하게 보호하면서 위험할 수 있는 외부의 네트워크에 접근할 수 있게 해주는 물리적 또는 개념적 서브넷이다. </p>
<p>DMZ를 사용하는 서비스는 WS와 WAS 서버를 분리한다. 정적 컨텐츠 등 사용자들이 접근하고, 사용자들에게 보이는 정보를 WS에 저장하고 처리하고, 보안이 중요한 사업 정보 등은 WAS에서 저장하고 처리한다. WS와 WAS 간 DMZ 네트워크를 정의하고, WS와 DMZ 그리고 DMZ와 WAS 사이에 각각 방화벽을 설치하여 들어오는 요청을 필터링한다. </p>
<p>WS를 통해 접근한 악의적인 요청은 첫번째 방화벽을 우선 거쳐야 하고, DMZ 존에 접근 했더라도 두번째 방화벽까지 뚫어야지만 기밀 정보에 접근할 수 있다. </p>
<p>또한, 보안이 중요한 서비스에서는 DMZ 존 내에 프록시 서버를 설치하여 DMZ 내부의 사용자 활동 모니터링, 사내 접근 부여 등 다양한 기능을 구현할 수 있다. 프록시 서버를 통해 요청을 중앙 집중 시킬 수 있어 모니터링 작업이 더 수월할 것이다. </p>
<h2 id="dmz의-장점은">DMZ의 장점은?</h2>
<p>결론부터 말하자면 보안 강화다. </p>
<p>공격자가 악의적인 패킷을 보내든, 내부 사설망 탐색을 시도하든, 결국 DMZ 존이라는 버퍼에 막힐 가능성이 높다. 네트워크 분리와 이중 방화벽을 통해 여러 공격이 필터링되고, 내부 사설망에 대한 정보를 더 철저하게 숨길 수 있다. </p>
<p>특히나 설계자에 따라 DMZ 존을 다양한 용도로 활용할 수 있기 때문에 맞춤형 보안 강화도 가능하다. 예를 들어 허가받은 IP주소에서 보낸 패킷인 척하는 IP Spoofing 공격은 패킷의 진위성을 검증하는 기능을 DMZ 존 내부에 구현하여 방어할 수 있다. </p>
<h2 id="dmz의-트렌드는">DMZ의 트렌드는?</h2>
<h4 id="클라우드의-발달">클라우드의 발달</h4>
<p>원래도 많은 기업이 DMZ를 활용해 내부 정보를 방어해왔다. </p>
<p>요즘은 많은 대형 기업이 서비스를 온프레미스에서 클라우드로 이전하거나 하이브리드로 운영하면서 가상머신과 컨테이너를 사용한다. 기업에서 웹서버를 직접 운영하기보다는 SaaS 서비스로 호스팅하는 경우가 증가했기에  이 서비스와 VPN으로 연결되는 DMZ 존을 두고 내부 웹 애플리케이션 서버를 운영하고는 한다. </p>
<blockquote>
<p><strong>VPN</strong>, 즉 가상 사설망은 클라이언트와 서버 사이에 위치해 클라이언트 요청에 대해 IP 주소 마스킹, 개인정보 암호화 등의 기능을 제공하여 서버의 방화벽 등을 우회할 수 있게끔 한다. </p>
</blockquote>
<h4 id="iot의-발달">IoT의 발달</h4>
<p>IoT와 OT의 발달은 산업의 발달로도 이어지지만, 보안 취약점을 증가시키기도 한다. 이를 보완하기 위해 DMZ 기반의 네트워크 분리로 기밀 정보를 보호할 수 있다. </p>
<h2 id="dmz를-뚫으려면">DMZ를 뚫으려면</h2>
<p>DMZ 존은 VPN을 이용해 광역 사설망의 패킷을 거를 수 있는데, 포트 포워딩을 통해 광역 사설망의 사용자도 DMZ 존으로 가려진 내부 사설망에 접근을 시도할 수 있다. </p>
<p>포트 포워딩은 라우터의 포트를 개방하고 연결이 허용되는 디바이스를 지정하여, 외부에서 직접적으로 연결할 수 있도록 허용한다. </p>
<p>물론 이 방식보다는 허가하는 클라이언트에 인증 권한을 부여하는 것이 나을 것이다. </p>
<hr />
<p><a href="https://aws.amazon.com/compare/the-difference-between-web-server-and-application-server/?nc1=h_ls">https://aws.amazon.com/compare/the-difference-between-web-server-and-application-server/?nc1=h_ls</a>
<a href="https://www.fortinet.com/resources/cyberglossary/what-is-dmz">https://www.fortinet.com/resources/cyberglossary/what-is-dmz</a>
<a href="https://azure.microsoft.com/en-us/resources/cloud-computing-dictionary/what-is-vpn">https://azure.microsoft.com/en-us/resources/cloud-computing-dictionary/what-is-vpn</a>
<a href="https://www.asus.com/support/faq/1001298/">https://www.asus.com/support/faq/1001298/</a></p>