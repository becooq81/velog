<h1 id="jdbc란">JDBC란?</h1>
<p>JDBC는 Java Database Connectivity의 약자로, 데이베이스와의 연결과 쿼리 수행을 제공하는 Java의 API(Application Programming Interface)입니다. </p>
<blockquote>
<p><strong>API</strong>(Application Programming Interface)는 두 소프트웨어 컴포넌트가 상호작용할 수 있도록 돕는 메커니즘입니다. 주로 일반적으로 요청을 보내는 클라이언트와, 요청에 대한 응답을 제공하는 서버라는 두 요소로 구성됩니다. API는 이 요청과 응답의 형식을 명확하게 정의하고, 각 구성 요소가 상대방의 내부 구현을 몰라도 서로 원활하게 소통할 수 있도록 합니다. 이 덕에 개발자들이 각 컴포넌트를 독립적으로 개발할 수 있죠.</p>
</blockquote>
<p>JDBC가 데이터베이스의 드라이버와 협력하여 API를 제공하는 덕에 개발자는 다양한 데이터베이스 시스템과의 호환성 걱정을 덜고, Java 애플리케이션에서 표준화된 방법으로 데이터베이스 작업을 수행할 수 있습니다.</p>
<h4 id="jdbc의-대표적인-기능-3가지">JDBC의 대표적인 기능 3가지</h4>
<ol>
<li>데이터베이스와 같은 데이터 소스와 연결</li>
<li>데이터베이스에 쿼리 전송</li>
<li>요청에 따른 데이터베이스 쿼리 결과 처리</li>
</ol>
<h4 id="주로-쓰이는-jdbc-api-클래스와-인터페이스">주로 쓰이는 JDBC API 클래스와 인터페이스</h4>
<ol>
<li><code>java.sql.Connection</code></li>
</ol>
<p><code>Connection</code> 객체는 Java 프로그램이 외부 데이터베이스 시스템과 연결할 때 사용됩니다. 데이터베이스와의 연결을 설정하고 유지하며, SQL 쿼리를 실행하거나 트랜잭션을 관리할 수 있습니다. </p>
<pre><code class="language-java">Connection connection = DriverManager.getConnection(url, username, password);</code></pre>
<p>데이터베이스 연결 생성 및 종료, 커밋/롤백 등 트랜잭션 관리, <code>Statement</code>/<code>PreparedStatement</code> 등 객체 생성 기능을 제공합니다. </p>
<p><code>setAutoCommit(true)</code>가 기본적으로 설정되어 있으나, 롤백 처리가 필요한 경우에는 <code>setAutoCommit(false)</code>로 설정하고, 상황에 따라 명시적으로 <code>rollback()</code> 또는 <code>commit()</code>을 호출할 수 있습니다.</p>
<ol start="2">
<li><code>java.sql.Statement</code></li>
</ol>
<p>SQL 쿼리를 실행하기 위한 가장 기본적인 인터페이스로, SQL 쿼리를 실행할 때마다 새롭게 컴파일되며, static 쿼리에 해당합니다. </p>
<p>쿼리를 직접 실행하므로 SQL Injection 공격에 취약합니다.</p>
<ul>
<li><code>public boolean execute(String sql) throws SQLException</code>: DML, Query, DDL 등 SQL문을 전반적으로 수행할 수 있는 메서드입니다.<ul>
<li>반환값이 <code>true</code>면 결과가 <code>ResultSet</code>임을 의미합니다.</li>
<li>반환값이 <code>false</code>면 결과가 DML이거나 결과가 없음을 의미합니다.</li>
</ul>
</li>
<li><code>public boolean executeQuery(String sql) throws SQLException</code>: <code>select</code>문을 사용할 때 쓰는 메서드입니다. </li>
<li><code>public int executeUpdate(String sql) throws SQLException</code>: <code>select</code> 문을 제외한 DML 쿼리를 수행할 때 사용하고, 쿼리에 의해 영향을 받은 행의 개수를 반환합니다. </li>
</ul>
<pre><code class="language-java">Statement statement = connection.createStatement();
ResultSet resultSet = statement.executeQuery(&quot;SELECT * FROM users WHERE id = 1&quot;);</code></pre>
<ol start="3">
<li><code>java.sql.PreparedStatement</code></li>
</ol>
<p>미리 컴파일된 SQL 쿼리를 실행하는 데 사용되는 쿼리로, 쿼리의 구조는 주로 고정되어 변수 값을 Java 메서드로 안전하게 삽입하여 <code>Statement</code>보다 보안이 좋습니다. </p>
<pre><code class="language-java">PreparedStatement preparedStatement = connection.prepareStatement(&quot;SELECT * FROM users WHERE id = ?&quot;);
preparedStatement.setInt(1, 1);
ResultSet resultSet = preparedStatement.executeQuery();</code></pre>
<blockquote>
<p><strong>SQL Injection</strong>은 애플리케이션 단에서 데이터베이스로 보내는 SQL 쿼리의 허점을 악용하는 데이터베이스 공격 기법입니다. PreparedStatement는 SQL 쿼리를 미리 컴파일하고, <code>?</code> 등의 placeholder로 파라미터를 받아 수행하기 때문에 삽입되는 데이터는 SQL문이 아닌, 일반적인 데이터로 취급됩니다. 
코드와 데이터의 분리로 인해 삽입된 데이터는 SQL 구조에 영향을 끼칠 수 없으며, SQL Injection에 흔히 사용되는 특수 문자 등도 철저히 데이터로만 취급되어 무시됩니다. </p>
</blockquote>
<p>또한, 쿼리가 미리 컴파일되기 때문에 동일 쿼리를 여러 번 실행될 때 성능이 향상됩니다. 이 때 <code>clearParameters()</code> 메서드로 인자 값을 초기화할 수 있습니다. </p>
<ol start="4">
<li><code>java.sql.ResultSet</code></li>
</ol>
<p>SQL 쿼리의 실행 결과를 저장하는 객체로, 테이블 형식으로 데이터를 저장합니다. 현재 데이터의 행을 가르키는 커서를 유지하는데, 이 커서가 처음에는 테이블의 첫 행 전을 가르키고, <code>next()</code> 메서드로 다음 행으로 넘어가며 이 행 이후에 또 데이터가 있는지 <code>boolean</code> 값을 반환합니다. 그래서 <code>while loop</code> 조건으로 <code>ResultSet</code>에 <code>.next()</code>를 사용하여 데이터를 애플리케이션 단에 받아오고는 하죠. </p>
<pre><code class="language-java">ResultSet resultSet = statement.executeQuery(&quot;SELECT * FROM users&quot;);
while (resultSet.next()) {
    int id = resultSet.getInt(&quot;id&quot;);
    String name = resultSet.getString(&quot;name&quot;); // getInt, getDate 등
}</code></pre>
<ol start="5">
<li><code>java.sql.Blob</code></li>
</ol>
<p>BLOB는 Binary Large Object의 약자로, 대용량의 이진 데이터를 저장하고 처리하기 위한 객체입니다. 주로 이미지, 비디오, 파일 등과 같은 큰 바이너리 데이터를 데이터베이스에 저장할 때 사용됩니다.</p>
<pre><code class="language-java">Blob blob = resultSet.getBlob(&quot;data&quot;);
InputStream inputStream = blob.getBinaryStream();</code></pre>
<ol start="6">
<li><code>java.sql.CallableStatement</code></li>
</ol>
<p>Stored Procedure를 호출합니다. </p>
<blockquote>
<p><strong>Stored Procedure</strong>는 저장되어 재사용될 수 있는, 준비된 SQL 코드입니다. 자주 쓰이는 SQL 질의는 stored procedure에 저장하여 단순 호출로 재수행할 수 있습니다.</p>
</blockquote>
<pre><code class="language-sql">CREATE PROCEDURE procedure_name
AS
sql_statement
GO;
EXEC procedure_name;</code></pre>
<p>이미 저장되어 있는 코드를 단순히 호출하기 때문에 속도가 더 빠를 수 있고, SQL 코드 없이 Java 코드만 사용하기 때문에 SQL에 독립적인 코딩이 가능합니다. </p>
<h2 id="jdbc의-구조">JDBC의 구조</h2>
<p>JDBC는 크게 애플리케이션과 JDBC manager 간 소통을 지원하는 JDBC API와, JDBC manager와 데이터베이스 드라이버 간 소통을 지원하는 JDBC driver, 두 부분으로 구분할 수 있습니다. </p>
<p>Java 애플리케이션은 JDBC API와 소통하고, JDBC API는 JDBC Driver와 통신하여, JDBC Driver는 해당 데이터베이스와 통신하죠.</p>
<p><img alt="" src="https://velog.velcdn.com/images/becooq81/post/d65ace54-889a-4de4-80b4-bd45d5c60764/image.png" />
출처: Medium</p>
<h4 id="1-jdbc-api">1. JDBC API</h4>
<p>여러 종류의, 다수의 데이터베이스와 분산 환경을 이뤄 사용할 수 있습니다. </p>
<h4 id="2-jdbc-driver-manager">2. JDBC Driver Manager</h4>
<p>JDBC <code>DriverManager</code> 클래스는 Java 애플리케이션을 JDBC Driver에 연결하는 객체를 정의합니다. </p>
<h4 id="3-jdbc-test-suite">3. JDBC Test Suite</h4>
<p>Test Suite는 테스트의 묶음을 의미합니다. 즉, JDBC Test Suite은 JDBC Driver가 잘 동작하는지, JDBC API의 주요 기능을 테스트해보는 역할을 수행합니다. </p>
<h4 id="4-jdbc-odbc-bridge">4. JDBC-ODBC Bridge</h4>
<p>ODBC는 Open Database Connectivity의 약자로, 언어 독립적인 데이터베이스 접근 표준입니다. Java에 한정된 기능을 제공하는 JDBC와 차이가 있죠.</p>
<p>Java Software Bridge는 ODBC driver를 통한 JDBC 접근을 제공합니다. 성능 등의 이유로 ODBC driver를 통한 접근은 잘 사용되지 않는 방법이죠. </p>
<h2 id="jdbc의-동작">JDBC의 동작</h2>
<ol>
<li>애플리케이션은 데이터베이스의 JDBC 자원을 얻기 위해 JNDI API를 호출합니다.</li>
<li>JDBC 자원을 통해 애플리케이션은 데이터베이스 연결을 얻습니다.</li>
<li>이 때부터 데이터베이스 조회, 수정, 삭제, 삽입이 가능해집니다.</li>
<li>애플리케이션이 데이터베이스 작업 완료 후에는 데이터베이스 연결을 닫고 커넥션 풀에 반납합니다.</li>
</ol>
<blockquote>
<p><strong>커넥션 풀</strong>은 데이베이스 커넥션을 미리 구비하고, 애플리케이션이 커넥션을 요청하거나 반납할 수 있습니다. 매번 요청이 들어온 순간부터 커넥션을 만들어 사용하는 것보다 효율적이며, 데이터 또는 클라이언트 수의 증가에 빠르게 대응할 수 있죠. </p>
</blockquote>
<h2 id="jdbc에-대한-결론">JDBC에 대한 결론</h2>
<p>JDBC를 사용하면 Java 코드로 데이터베이스를 관리할 수 있는 장점이 있지만, 드라이버 설정, 연결 관리, SQL 쿼리 작성, 그리고 쿼리 결과 처리와 같은 작업들을 직접 처리해야 하는 번거로움이 있습니다. 이러한 반복적이고 오류가 발생하기 쉬운 작업들을 개발자가 직접 관리해야 하다 보니, 생산성을 높이고 코드를 더 간결하게 만들기 위해 JDBC의 복잡한 작업들을 자동으로 처리해주는 여러 프레임워크가 등장했습니다.</p>
<p><img alt="" src="https://velog.velcdn.com/images/becooq81/post/9d404798-9a16-4a3b-80b8-459d2958fad9/image.png" /></p>
<h1 id="orm">ORM</h1>
<p>Object-Relational Mapping의 약자인 ORM은 객체지향적으로 데이터베이스에 질의하고 데이터를 처리하는 기술입니다. </p>
<p>ORM 라이브러리는 주로 데이터를 처리하기 위해 필요한 코드(SQL문 포함)를 캡슐화하여 이 라이브러리를 사용하는 개발자들은 SQL문 없이 그 라이브러리의 언어로만 데이터를 조작할 수 있게 해줍니다. </p>
<h2 id="orm을-사용하는-이유">ORM을 사용하는 이유</h2>
<h4 id="1-dry-dont-repeat-yourself">1. DRY: Don't Repeat Yourself</h4>
<p>ORM을 사용하면 데이터 모델을 한 곳에 정의하고 이를 통해 데이터베이스와 상호작용합니다. 매번 SQL 쿼리를 작성하는 대신, 모델을 통해 데이터 조회/삽입/삭제 등을 반복적으로 사용할 수 있어 코드 중복이 줄어듭니다.</p>
<h4 id="2-데이터베이스-독립성을-보장한다">2. 데이터베이스 독립성을 보장한다</h4>
<p>특정 DBMS에 의존적인 SQL문법도 추상화되어 DBMS를 바꾸더라도 최소한의 변경사항만으로 프로젝트를 정상적으로 수행할 수 있습니다.</p>
<h4 id="3-테이블-관리가-쉬워진다">3. 테이블 관리가 쉬워진다</h4>
<p>ORM은 엔티티 매핑으로 테이블을 자동으로 생성하는 등 변경 사항을 자동으로 반영해주는 도구를 제공해서 데이터베이스 관리가 쉬워집니다.</p>
<h4 id="4-mvc-아키텍쳐를-강제한다">4. MVC 아키텍쳐를 강제한다</h4>
<p>데이터 모델을 통해서 데이터베이스를 관리해야 하기 때문에 비즈니스 로직을 처리하는 레이어와 자연스럽게 분리됩니다.</p>
<p>역할의 분리는 곧 유지보수와 테스트 등의 용이성으로 이어집니다.</p>
<h4 id="5-최소한의-보안과-쿼리-최적화가-보장된다">5. 최소한의 보안과 쿼리 최적화가 보장된다.</h4>
<p>키워드는 최소한입니다. 당연히 숙련된 개발자가 짜는 코드가 더 성능이 좋을 것이지만, 일정 수준 이상의 보안과 성능을 보장받을 수 있습니다.</p>
<h4 id="6-언어의-객체지향성을-보장하며-데이터베이스와-매핑할-수-있다">6. 언어의 객체지향성을 보장하며 데이터베이스와 매핑할 수 있다.</h4>
<p>ORM은 객체지향 언어와 관계형 데이터베이스 간의 간극을 해소하여, 데이터베이스 조작을 더 용이하게 해줍니다.</p>
<p>객체로 데이터베이스의 레코드를 다룰 수 있게 해주어 개발자는 객체의 속성 및 메서드에 집중하여 코드를 짤 수 있습니다.</p>
<p>예를 들어 상속과 같이 관계형으로 표현하기 까다로워지는 엔티티 관계도 ORM으로 간단하게 매핑될 수 있습니다. </p>
<h2 id="orm의-단점">ORM의 단점</h2>
<h4 id="1-숙련된-데이터베이스의-관리자가-더-좋은-성능의-쿼리를-짤-것입니다">1. 숙련된 데이터베이스의 관리자가 더 좋은 성능의 쿼리를 짤 것입니다</h4>
<h1 id="hibernate">Hibernate</h1>
<p>Hibernate은 Java를 위한 ORM 프레임워크입니다. JDBC만 활용하면 개발자가 SQL문을 직접 짜야하는 반면에, Hibernate은 ORM 프레임워크기 때문에 개발자는 Java의 객체지향성에 집중하여 Java로만 개발할 수 있죠. </p>
<p>하지만 그렇다고 해서 JDBC에 대한 의존성이 사라진 것은 아닙니다. Hibernate 또한 JDBC를 통해 데이터베이스와 상호작용하고, 사실 JDBC API 위에 만들어졌기 때문이죠. 하지만 Hibernate이 JDBC API를 추상화해주는 덕에 개발자는 더 쉽고 편하게 데이터베이스를 관리할 수 있습니다.</p>
<p>다만, Hibnerate이 제공하는 추상화와 편리함이 섬세한 데이터베이스 관리가 필요한 작업에서는 너무 많은 것을 숨길 수도 있습니다.</p>
<h1 id="jpa">JPA</h1>
<p>그렇다면 JPA(Java Persistence API)와 Hibernate의 차이는 무엇일까요?</p>
<p>간단히 말하자면 JPA는 명세고, Hibernate은 이에 맞춘 구현입니다. JPA라는 하나의 ORM 명세 표준에 대한 여러 구현 프레임워크 중 하나가 Hibernate인 셈이죠.</p>
<p>하지만 명세에서 요구되지 않은 기능이 Hibernate에 구현되어 개발자들은 Hibernate과 JPA 중 선택의 기로에 놓이는 아이러니한 상황도 발생한답니다.</p>
<h2 id="jpa에-관하여">JPA에 관하여</h2>
<p>JPA는 단순히 어떻게 ORM을 구현해야 하는가에 대한 약속만 정의하여 구현체가 없는, 추상적인 인터페이스로 구성되어 있습니다. 그래서 실질적인 기능은 제공하지 않죠.</p>
<p>JPA는 ORM의 일관된 표준화를 추구하여 개발자들이 일관된 API를 사용하고, 특정 프레임워크에 종속되지 않는 코드를 작성할 수 있도록 합니다. </p>
<p><code>@Entity</code>, <code>@Table</code> 등 객체와 데이터베이스 간 매핑 정의, 영속성 컨텍스트 관리, 트랜잭션 등을 모두 정의하죠. </p>
<h2 id="persistence에-관하여">Persistence에 관하여</h2>
<p>Java도 알겠고, API도 알겠는데, 그럼 Persistence는 무엇일까요?</p>
<p>Persistence(영속성 컨텍스트)는 애플리케이션이 종료된 후에도 그 애플리케이션이 생성한 데이터가 저장된다는 개념입니다. </p>
<p>영속성 컨텍스트는 특성에 따라 1개 이상의 엔티티 매니저와 연관되어 엔티티 인스턴스와 그 라이프사이클이 관리되는 공간이기도 합니다. </p>
<p>영속성 컨텍스트는 각 엔티티 인스턴스가 생성, 저장, 삭제되는 범위를 정의합니다. 또한, 영속성 엔티티 집합을 소유하는 캐쉬와도 같습니다. 하나의 트랜잭션이 완료되면 persistent 객체는 모두 persistent context으로부터 준영속 상태가 되어 더이상 관리되지 않습니다. </p>
<h2 id="jpa의-구성">JPA의 구성</h2>
<h4 id="1-persistence-unit">1. Persistence unit</h4>
<p>Persistence unit은 Java 클래스가 관계형 데이터베이스에 어떻게 매핑되는지 정의하고, 데이터베이스 연결 설정, 트랜잭션 관리 등에 대한 정보를 포함합니다.</p>
<p><code>EntityManagerFactory</code>는 이 데이터로 영속성 컨텍스트를 만들어 <code>EntityManager</code>를 통해 제공합니다.</p>
<h4 id="2-entitymanagerfactory">2. EntityManagerFactory</h4>
<p><code>EntityManagerFactor</code>는 데이터베이스 작업을 위한 <code>EntityManager</code> 인스턴스를 생성합니다. </p>
<h4 id="3-persistence-context">3. Persistence context</h4>
<p>영속성 컨텍스트는 엔티티 인스턴스의 라이프사이클을 관리하는 런타임 환경입니다. 즉, 현재 애플리케이션이 조작하는 활성 엔티티 인스턴스의 집합을 보유합니다. 이 컨텍스트는 엔티티의 변경 사하을 추적하고, 데이터베이스와의 상태를 관리합니다.</p>
<p>수동으로 생성하거나 의존성 주입으로 얻을 수 있으며, 주로 애플리케이션 서버에 의해 관리됩니다. </p>
<blockquote>
<p>엔티티는 라이프사이클을 거칩니다.
<img alt="" src="https://velog.velcdn.com/images/becooq81/post/845334e2-3def-49a4-ba9c-2fdb524be67d/image.png" />
<a href="https://vladmihalcea.com/wp-content/uploads/2014/07/jpaentitystates.png">출처</a></p>
</blockquote>
<ol>
<li>비영속(Transient): 엔티티가 새로 생성되어 아직 영속성 컨텍스트에 저장되지 않은 상태. </li>
<li>영속(Persistent): 영속성 컨텍스트에 저장된 상태. 어떠한 변경이 일어나면 캐시에 반영됩니다.</li>
<li>준영속(Detached): 영속 상태에서 데이터베이스와의 연결이 끊어진 상태. 데이터베이스와의 동기화가 이루어지지 않습니다. 예를 들어 세션이 종료되거나 명시적으로 분리된 상태입니다.</li>
<li>삭제(Removed): 아직은 영속성 컨텍스트에 있는 엔티티가 데이터베이스에서 삭제될 상태입니다.</li>
</ol>
<h4 id="4-entitymanager">4. EntityManager</h4>
<p><code>EntityManager</code>는 애플리케이션과 영속성 컨텍스트를 잇는 역할을 수행합니다. 엔티티 인스턴스를 생성, 수정, 읽기, 삭제하는 메서드를 제공하며, 객체와 관계형 간 매핑의 메타데이터를 관리합니다.</p>
<p><code>EntityManager</code>의 인스턴스는 의존성 주입 또는 <code>EntityManagerFactory</code>에서 직접 얻을 수 있습니다. </p>
<h4 id="5-entity-객체들">5. Entity 객체들</h4>
<p>엔티티 객체는 데이터베이스 테이블의 행 하나를 표현하는 단순한 Java 클래스입니다. </p>
<h2 id="jpa-사용하기">JPA 사용하기</h2>
<h4 id="1-엔티티-영속하기">1. 엔티티 영속하기</h4>
<p>Hibernate으로 영속하기</p>
<pre><code class="language-java">DomesticCat fritz = new DomesticCat();
fritz.setColor(Color.GINGER);
fritz.setSex('M');
fritz.setName(&quot;Fritz&quot;);
session.save(fritz);</code></pre>
<p>JPA로 영속하기</p>
<pre><code class="language-java">DomesticCat fritz = new DomesticCat();
fritz.setColor(Color.GINGER);
fritz.setSex('M');
fritz.setName(&quot;Fritz&quot;);
entityManager.persist(fritz);</code></pre>
<h4 id="2-엔티티-삭제하기">2. 엔티티 삭제하기</h4>
<pre><code class="language-java">// Hibernate
Book book = new Book();
book.setAuthor( session.load( Author.class, authorId ) );

// JPA
Book book = new Book();
book.setAuthor( entityManager.getReference( Author.class, authorId ) );</code></pre>
<h4 id="3-영속-상태-관리하기-강제-저장하기">3. 영속 상태 관리하기 (강제 저장하기)</h4>
<p>영속 컨텍스트는 메모리에 저장되고, 간헐적으로 엔티티 매니저에 의해 데이터베이스와 동기화됩니다. 이 과정을 <code>flushing</code>이라고도 하죠.</p>
<p>기본적으로 플러쉬는 다음과 같은 상황에 수행됩니다.</p>
<ol>
<li>쿼리 수행 전</li>
<li><code>java.persistence.EntityTransaction.commit()</code>이 호출되었을 때</li>
<li><code>EntityManager.flush()</code>가 호출되었을 때</li>
</ol>
<p>플러쉬에 의해 SQL문은 다음과 같은 순서로 수행됩니다.</p>
<ol>
<li>모든 엔티티 삽입: <code>EntityManager.persist()</code>가 사용된 순서를 유지하여 삽입합니다.</li>
<li>모든 엔티티 수정 작업</li>
<li>모든 컬렉션 삭제 작업</li>
<li>모든 컬렉션 요소 삭제/수정/삽입</li>
<li>모든 컬렉션 삽입 작업</li>
<li>모든 엔티티 삭제 작업: <code>EntityManager.remove()</code>가 사용된 순서를 유지하여 삭제합니다.</li>
</ol>
<blockquote>
<p>단, 애플리케이션에 의해 결정된 식별자를 사용하는 엔티티 인스턴스는 <code>save</code>되었을 때 삽입됩니다.</p>
</blockquote>
<p>결론적으로, <code>flush()</code> 메서드를 명시적으로 호출하지 않는 이상, 엔티티 매니저가 즉각적으로 데이터베이스와 동기화될 거라는 보장은 없습니다. </p>
<p>하지만, Hibernate은 <code>Query.getResult()</code>, <code>Query.getSingleResult()</code>의 메서드가 꼭 최신의 데이터를 반환하는 것을 보장합니다. </p>
<h1 id="jpql">JPQL</h1>
<p>Java Persistence Query Language(JPQL)은 JPA가 제공하는 객체 지향 쿼리 언어로, 데이터베이스 테이블 대신 JPA 엔티티 객체를 대상으로 쿼리를 수행합니다. SQL과 유사한 문법을 사용하지만, 데이터베이스 테이블이 아닌, 엔티티의 필드와 관계를 기준으로 작동합니다. </p>
<h2 id="jpql의-장점">JPQL의 장점</h2>
<h4 id="1-데이터베이스-구조에-직접-의존하지-않습니다">1. 데이터베이스 구조에 직접 의존하지 않습니다.</h4>
<p>JPQL은 데이터베이스 스키마에 직접 의존하지 않고, 객체 모델을 기반으로 쿼리를 작성하기 때문에 엔티티 모델에 의존합니다.</p>
<h4 id="2-엔티티-간-관계를-단순하게-표현하고-사용할-수-있습니다">2. 엔티티 간 관계를 단순하게 표현하고, 사용할 수 있습니다.</h4>
<p>JPQL은 객체 모델을 그대로 활용하기 때문에 일대일, 일대다, 상속, 다형성 등 객체 간의 관계를 보다 쉽게 다룰 수 있습니다. </p>
<p>1:1, 1:N 등 관계를 표현하기 위해서는 여러 조인 연산을 필요로 하는 SQL문에 비해 큰 장점이죠.</p>
<h4 id="3-dbms-독립성을-보장합니다">3. DBMS 독립성을 보장합니다.</h4>
<h2 id="jpql의-단점">JPQL의 단점</h2>
<h4 id="1-특정-dbms에-의존적인-기능을-사용하지-못합니다">1. 특정 DBMS에 의존적인 기능을 사용하지 못합니다.</h4>
<p>JPA에 데이터베이스 추상화를 한 레이어 더 추가했기 때문에 JPA에서는 네이티브 쿼리로 가능했던 특정 DBMS에 의존적인 기능도 JPQL에서는 사용할 수 없습니다. </p>
<h4 id="2-성능을-보장하기-어렵습니다">2. 성능을 보장하기 어렵습니다.</h4>
<p>JPA 구현체가 JPQL 쿼리를 SQL문으로 번역하는 과정에서 JPA 구현체가 자동으로 쿼리 최적화를 시도하지만, 항상 효율적인 것은 아닙니다. 개발자가 직접 작성한 SQL문만큼의 성능을 보장하기 어렵고, 예상치 못한 성능 저하가 발생할 수 있습니다.</p>
<h2 id="jpql-동작-방식">JPQL 동작 방식</h2>
<ol>
<li>애플리케이션이 <code>javax.persistence.EntityManager</code> 인터페이스의 인스턴스를 생성합니다.</li>
<li><code>EntityManager</code>는 <code>javax.persistence.Query</code> 인터페이스의 인스턴스를 생성합니다 (예) <code>createNamedQuery</code></li>
<li><code>Query</code> 인스턴스가 쿼리를 수행합니다.</li>
</ol>
<h2 id="jpql의-종류">JPQL의 종류</h2>
<h4 id="1-dynamic-query-동적-쿼리">1. Dynamic Query (동적 쿼리)</h4>
<p>동적 쿼리는 런타임 시점에 애플리케이션의 요구에 따라 동적으로 생성되는 쿼리입니다. </p>
<h4 id="2-named-query">2. Named Query</h4>
<p>네임드 쿼리는 동일 쿼리를 여러 번 호출하는 상황에서 쓰이기 위한 쿼리로, <code>name</code> 속성으로 식별되고, <code>query</code> 속성에 쿼리 문을 담습니다.</p>
<p>네임드 쿼리는 컴파일된 상태에서 재호출하기 때문에 런타임 동안 성능이 더 낫고, 같은 쿼리문을 다시 작성할 필요를 줄여 코드 재사용성도 향상합니다. </p>
<h1 id="querydsl">QueryDSL</h1>
<p>JPQL의 주요 단점 중 하나는, 쿼리 문자열에 오타 혹은 문법적인 오류가 컴파일 타임이 아닌 런타임 시점에 검출된다는 점입니다. (정적 쿼리일 경우에는 애플리케이션 로딩 시점에 검출됩니다.)</p>
<p>QueryDSL은 정적 타입으로 SQL 등 쿼리를 생성하는 프레임워크로, 이 문제점을 다음과 같이 해결하고자 시도합니다.</p>
<ol>
<li>문자가 아닌 코드로 쿼리를 작성해서 컴파일 시점에 문법 오류를 검출합니다. </li>
<li>동적 쿼리의 작성이 더 편리합니다.</li>
<li>쿼리 작성 시 제약 조건 등을 메서드로 추출하여 코드 재사용성을 높입니다.</li>
</ol>
<h2 id="querydsl-동작-방식">QueryDSL 동작 방식</h2>
<ol>
<li>QueryDSL은 프로젝트 내의 <code>@Entity</code> 선언 클래스를 탐색합니다.</li>
<li><code>JPAAnnotationProcessor</code>를 사용해 각 엔티티에 대한 Q 클래스를 생성합니다. Q 클래스는 엔티티의 각 필드와 메서드를 정적 타입으로 제공합니다.</li>
</ol>
<p>예를 들어, <code>User</code> 엔티티가 있다면, <code>QUser</code>라는 클래스가 생성되어 <code>name</code>, <code>age</code>와 같은 필드에 접근할 수 있습니다.</p>
<ol start="3">
<li>Q 클래스를 통해 쿼리를 생성하고 실행하며, 이 과정에서 SQL/JPQL 등 쿼리가 자동생성됩니다. </li>
</ol>
<pre><code class="language-java">// EntityManager를 주입받았다고 가정
public List&lt;User&gt; findUsersByName(EntityManager entityManager, String name) {
    QUser user = QUser.user; // QUser 인스턴스 생성

    // QueryDSL을 사용한 쿼리 작성
    List&lt;User&gt; result = new JPAQuery&lt;User&gt;(entityManager)
                            .select(user)
                            .from(user)
                            .where(user.name.eq(name)) // 정적 타입으로 필드 접근
                            .fetch();
    return result;
}</code></pre>
<h1 id="마치며">마치며</h1>
<p>JDBC, JPA, JPQL, QueryDSL 모두 Java 애플리케이션에서 데이터베이스와 상호작용하는 데 필수적인 도구들입니다. 각기 다른 문제사항, 개발자의 목적 등을 고려하고 이 도구들을 적절히 조합하여 애플리케이션의 성능과 유지보수성, 개발편리성을 모두 충족할 수 있을 것이라 생각합니다. </p>
<hr />
<p><a href="https://aws.amazon.com/what-is/api/">AWS: What is What is an API (Application Programming Interface)?</a>
<a href="https://www.geeksforgeeks.org/introduction-to-jdbc/">GeeksForGeeks: Introduction to JDBC</a>
<a href="https://medium.com/@Bharat2044/what-is-jdbc-introduction-to-java-database-connectivity-649677818a8b">Medium: Introduction to Java Database Connectivity</a>
<a href="https://docs.python.org/ko/3.7/library/unittest.html#:~:text=%ED%85%8C%EC%8A%A4%ED%8A%B8%20%EB%AC%B6%EC%9D%8C(test%20suite)%EC%9D%80,%EC%A2%85%ED%95%A9%ED%95%98%EB%8A%94%20%EB%8D%B0%20%EC%82%AC%EC%9A%A9%EB%90%A9%EB%8B%88%EB%8B%A4.">Python Docs: unittest — 단위 테스트 프레임워크</a>
<a href="https://www.w3schools.com/sql/sql_stored_procedures.asp">W3 Schools: SQL Stored Procedures for SQL Server</a>
<a href="https://docs.oracle.com/javase/7/docs/api/java/sql/CallableStatement.html">Oracle Docs: Interface CallableStatement</a>
<a href="https://docs.oracle.com/javase/8/docs/api/java/sql/ResultSet.html">Oracle Docs: Interface ResultSet</a>
<a href="https://stackoverflow.com/questions/68702250/jdbc-and-hibernate-used-for-same-purpose">Stack Overflow: JDBC and Hibernate used for same purpose? (Answered)</a>
<a href="https://stackoverflow.com/questions/1279613/what-is-an-orm-how-does-it-work-and-how-should-i-use-one">Stack Overflow: What is an ORM, how does it work, and how should I use one? [closed]</a>
<a href="https://www.theserverside.com/video/Hibernate-vs-JDBC-How-do-these-database-APIs-differ">The Server Side: Hibernate vs. JDBC How do these database APIs differ</a>
<a href="https://docs.oracle.com/cd/E19830-01/819-4712/ablii/index.html#:~:text=Each%20JDBC%20resource%20specifies%20a,application%20gets%20a%20database%20connection.">Oracle Help Center: About JDBC Resources and Connection Pools</a>
<a href="https://www.ibm.com/docs/en/was-liberty/nd?topic=liberty-java-persistence-api-jpa">IBM: Java Persistence API (JPA)</a>
<a href="https://www.ibm.com/docs/en/radfws/9.7?topic=architecture-jpa-query-language">IBM: JPA Query Language</a>
<a href="https://docs.jboss.org/hibernate/entitymanager/3.6/reference/en/html/objectstate.html">Hibernate Documentation: Chapter 3. Working with Objects</a>
<a href="https://tecoble.techcourse.co.kr/post/2021-08-08-basic-querydsl/">Tecoble: Spring Boot에 QueryDSL을 사용해보자</a></p>