<p>Java의 SOLID 원칙을 따라 객체지향적으로 프로그래밍하는 것은 좋은 Java 개발자가 되기에 필수적이다. SOLID 원칙이 생소할 수는 있지만, Java로 곧잘 개발하는 사람이라면 이미 원칙에 맞춰 코드를 짜고 있었을 수도 있다. </p>
<h1 id="single-responsibility-principle-srp">Single Responsibility Principle (SRP)</h1>
<p>단일 책임의 원칙이다. 즉, 각 클래스는 단 하나의 목적(또는 역할)을 가져야 한다.</p>
<p>클래스는 다른 클래스의 변화에 의해 수정되면 안 된다. 자신의 목적의 변화에만 영향을 받아야 한다. </p>
<p>예를 들어, Java에는 <code>Date</code> 클래스와 <code>DateFormat</code> 클래스가 존재한다. 날짜 객체를 관리하는 클래스와 날짜 객체의 포맷을 관리하는 클래스로 나눠서 각각 개별의 역할을 배정한 것이다.</p>
<pre><code class="language-java">Date d = new Date();
String s = DateFormat.getDateInstance().format(d);
System.out.println(s);</code></pre>
<p>시스템에서 표현되는 날짜를 변경하고 싶으면 <code>Date</code> 클래스만 수정하면 되고,
디스플레이에 보이는 날짜의 포맷을 변경하고 싶으면 <code>DateFormat</code> 클래스만 수정하면 된다.</p>
<p>각 수정 사항에 대해 영향을 받는 범위를 최소한으로 줄였기에 버그 또는 의도치 않은 문제가 발생될 확률이 확연히 낮아진다.</p>
<p>이 두 클래스를 한 데 합쳤으면 어땠을까? 필요 이상으로 거대한 클래스가 됐을 것이다. 날짜 포맷을 바꾸기 위해 코드를 수정했더니 날짜 객체까지 영향을 미쳐버리는 경우도 발생할 가능성이 높아진다.</p>
<h1 id="open-closed-principle">Open-Closed Principle</h1>
<p>확장에는 열려 있지만, 변화에는 닫혀있다.</p>
<p>즉, 존재하는 클래스를 직접 수정하기 보다는 상속 또는 위임을 통해 클래스를 활용하고 확장해야 한다.</p>
<p>이미 잘 돌아가는 클래스를 굳이 수정해야 할까? 특히 그 클래스를 상속하는, 또는 그 클래스의 인스턴스를 활용하는, 의존적인 타 클래스가 존재하는 경우에는 더 신중해야 한다. 이 클래스의 변경사항은 곧 이 클래스에 의존하는 다른 클래스에도 반영되고, 오류로 이어질 수 있다.</p>
<p>상속을 활용하면 새로운 코드(변경사항)가 기존의 클래스에 영향을 끼치지 않도록 방지하면서 새로운 기능을 추가할 수 있다. </p>
<p>이는 코드의 재사용과 유지보수성 면에서도 좋다.</p>
<h1 id="liskov-substitution-principle">Liskov Substitution Principle</h1>
<p>리스코프 치환 원칙</p>
<p>부모 클래스의 객체는 하위 클래스의 객체로 대체될 수 있어야 된다는 뜻인데, 이 때 프로그램의 동작 과정 및 결과에 변화가 있으면 안된다.</p>
<p>상속을 활용해서 부모 클래스의 메서드를 자식 클래스가 오버라이딩해서 두 메서드가 다른 결과를 내는 경우 리스코프 치환 법칙에 위반되는 코드다. </p>
<h3 id="리스코프-치환-법칙의-중요성">리스코프 치환 법칙의 중요성</h3>
<p>이렇게 리스코프 치환 법칙을 따르면 새로운 기능을 추가하기 꽤나 번거로워지는 것 같은데, 이 법칙을 따르는 것이 왜 좋을까? 왜 중요할까?</p>
<p>이 질문을 대답하려면 Open-Close 원칙을 다시 방문하면 된다. </p>
<p>우리는 Open-Close 원칙을 통해 변경에는 닫혀있지만 확장에는 열려있는 코드에 대해 배웠다. </p>
<p>예를 들어, 서비스 클래스가 모든 차 클래스들에 대해 각각 대응하는 코드는 수정과 확장에 매우 민감하다. 그래서 공통이 되는 속성 및 메서드를 뽑아서 베이스 클래스를 만들고, 서비스 클래스는 이 베이스 클래스에만 대응하도록 하여 세부 클래스들에 대한 의존성을 제거하는 것이다.</p>
<p>이러한 방식으로 클래스들 간 구조를 계층화 하였을 때의 리스크는 부모 클래스 형으로 선언된 객체가 자식 클래스로 인스턴스화되었을 때, 부모 클래스의 메서드 호출이 잘 동작하는가? 이다. </p>
<p><img alt="" src="https://velog.velcdn.com/images/becooq81/post/4c79ccb1-bdc1-45e8-84be-095f6b6d767d/image.png" />
출처: baeldung</p>
<p>위 사진과 같은 계층 구조로 은행 계좌 클래스를 구성했을 때, 서비스 클래스는 계좌 (베이스) 클래스만 사용한다. </p>
<p>새로운 클래스, 정기적금 계좌 클래스도 계좌 클래스를 상속한다 가정하자. <code>FixedTermDepositAccount</code> 클래스는 정기 적금 계좌라서 현금 인출이 불가하고, <code>withdraw</code> 메서드를 구현하지 않는다. </p>
<p>그래서 서비스 클래스는 <code>Account</code> 클래스의 동작 과정을 예측하고 <code>withdraw</code> 메서드를 호출할 텐데, 해당 객체가 <code>FixedTermDepositAccount</code> 클래스로 인스턴스화되어 메서드를 제대로 호출하지 못하는 결과가 발생한다.</p>
<p>이러한 상황이 발생하지 않는 것이 이상적이겠지만, 상속 관계를 설계하다보면 베이스 클래스에는 있는 메서드가 자식 클래스에는 필요 없을 수도 있다. 해당하는 메서드에 대해서는 <code>UnsupportedOperationException</code>을 발생시키는 것도 방법이다.</p>
<h1 id="interface-segregation-principle">Interface Segregation Principle</h1>
<p>각 클래스는 자신이 필요로 하지 않는 인터페이스에 의해 강요받지 않아야 한다.</p>
<p>구현해야 할 메서드들을 모두 하나의 인터페이스에 정의한다면 이 인터페이스를 구현하는 클래스는 필요하지도 않은 메서드들 또한 구현을 강요 받는다.</p>
<p>하나의 큰 인터페이스를 여러 클래스에 강요하는 것보다, 각 인터페이스를 최소한의 크기로 유지하여 이를 구현하는 클래스는 자신이 필요로 하는 기능만 구현하도록 하는 것이 인터페이스 분리 원칙이다.</p>
<h1 id="dependency-inversion-principle">Dependency Inversion Principle</h1>
<p>상위 모듈과 하위 모듈이 서로에게 의존해서는 안된다. 모두 추상화에 의존하여 동작해야 한다. 
또한, 추상화가 구현에 의존해서는 안된다. 구현이 추상화에 의존하는 방식을 따라야 한다.</p>
<p>JDBC 연결을 생각해보자. DriverManager와 DataSource 등이 데이터베이스에 의존하는 상세 디테일을 모두 구현하고 추상화된 인터페이스를 제공하기 때문에 JDBC를 활용할 때 하위 모듈의 구현을 신경쓰지 않아도 된다. 어느 데이터베이스를 사용하는 지와 무관하게 사용이 간편하다. </p>
<p>의존성의 분리를 코드에 구현하기 위해 인스턴스화를 하지 않는 방법도 있다. </p>
<p><code>Keyboard</code> 클래스와 <code>Monitor</code> 클래스를 필드로 갖는 <code>WindowMachine</code> 클래스를 가정해보자.</p>
<pre><code class="language-java">public class Windows98Machine {

    private final StandardKeyboard keyboard;
    private final Monitor monitor;

    public Windows98Machine() {
        monitor = new Monitor();
        keyboard = new StandardKeyboard();
    }

}</code></pre>
<p>생성자에서 모니터와 키보드 객체를 인스턴스화하기 때문에 <code>Monitor</code>, <code>Keyboard</code>, <code>WindowsMachine</code> 클래스는 모두 서로에게 의존하는 관계에 놓였다.</p>
<p>하지만, 인스턴스화를 방지하고, 각 필드를 파라미터로 받아서 사용한다면?
그리고 <code>Monitor</code>와 <code>Keyboard</code>를 인터페이스로 선언한다면?</p>
<p>=&gt; <code>Monitor</code>와 <code>Keyboard</code>를 구현하는, 확장하는 클래스까지 인자로 받아서 사용할 수 있어 확장성이 보장되는 동시에, 그 클래스들의 내부 구현에 영향을 받지 않아 유지보수성까지 좋다.</p>
<pre><code class="language-java">public class Windows98Machine{

    private final Keyboard keyboard;
    private final Monitor monitor;

    public Windows98Machine(Keyboard keyboard, Monitor monitor) {
        this.keyboard = keyboard;
        this.monitor = monitor;
    }
}</code></pre>
<hr />
<p>5개의 원칙으로 나뉜 SOLID지만, 예시를 구상해보며 상당 부분 겹친다는 점이 인상적이다.</p>
<p>진정히 SOLID한 코드를 짜보자</p>
<hr />
<p><a href="https://blogs.oracle.com/javamagazine/post/curly-braces-java-solid-design">https://blogs.oracle.com/javamagazine/post/curly-braces-java-solid-design</a>
<a href="https://www.baeldung.com/java-liskov-substitution-principle#:~:text=The%20Liskov%20Substitution%20Principle%20helps,follow%20the%20Open%2FClosed%20principle">https://www.baeldung.com/java-liskov-substitution-principle#:~:text=The%20Liskov%20Substitution%20Principle%20helps,follow%20the%20Open%2FClosed%20principle</a>.
<a href="https://www.baeldung.com/solid-principles">https://www.baeldung.com/solid-principles</a></p>