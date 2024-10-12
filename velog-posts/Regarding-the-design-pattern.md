<h1 id="디자인-패턴이란">디자인 패턴이란?</h1>
<p>디자인 패턴은 개발하면서 반복적으로 발생하는 문제들에 대한 해결책을 제시한다.</p>
<p>선배 개발자도 현재 우리가 만난 문제와 똑같거나 비슷한 문제를 겪고, 해결하는 과정에서 이를 패턴으로 만들어간 것이다.</p>
<h2 id="디자인-패턴의-분류">디자인 패턴의 분류</h2>
<p>디자인 패턴은 용도에 따라 분류할 수 있다: 생성, 행동, 구조</p>
<h3 id="생성-패턴-creational-pattern">생성 패턴 (Creational Pattern)</h3>
<p>객체 인스턴스를 생성하는 패턴. </p>
<p>(ex) Singleton, Factory, Prototype, Builder etc.</p>
<h4 id="1-싱글턴-패턴-singleton-pattern">1. 싱글턴 패턴 (Singleton Pattern)</h4>
<p>특정 클래스에 객체 인스턴스가 하나만 만들어지도록 하는 패턴</p>
<p>전역 변수 쓰듯이 이 객체 인스턴스를 어디서든지 접근할 수 있도록 메서드를 제공한다 </p>
<p>생성자의 접근자를 <code>private</code>로 제한하고, 클래스 내에서 <code>private static</code>한 객체를 하나 생성한 다음, 외부에서 이 객체에 접근할 수 있는 <code>getter</code> 메서드를 제공한다.</p>
<pre><code class="language-java">public class HouseDaoImpl {
    private static HouseDaoImpl impl = new HouseDaoImpl();

    private HouseDaoImpl() {}

    public static HouseDaoImpl getImpl() { return impl; }

    ...

}</code></pre>
<p>용도</p>
<ul>
<li>공유 자원(데이터베이스 등)에 대한 접근 제한 등을 위해 클래스의 인스턴스 수를 하나로 제한할 때</li>
</ul>
<p>장점</p>
<ul>
<li>클래스가 하나의 인스턴스만 갖도록 한다</li>
<li>단일 인스턴스에 대한 전역 접근 지점을 제공한다</li>
</ul>
<p>단점</p>
<ul>
<li>다중 스레드 환경에서 여러 스레드가 싱글턴 객체를 여러 번 생성하지 않도록 하기 위해서는 별도의 처리가 필요하다</li>
<li>유닛 테스트하기 까다로울 수 있다 </li>
</ul>
<h4 id="2-추상-팩토리-패턴-abstract-factory-pattern">2. 추상 팩토리 패턴 (Abstract Factory Pattern)</h4>
<p>구상(implementation) 클래스에 의존하지 않고도 서로 연관되거나 의존적인 객체로 이루어진 제품군을 생산하는 인터페이스를 제공한다. </p>
<p>추상 팩토리 패턴의 요소</p>
<ul>
<li><strong>추상 제품</strong>: 제품군를 구성하는 각 연관 제품 집합에 대한 인터페이스 <ul>
<li>(예) <code>Char</code> 인터페이스는 <code>VictorianChair</code>, <code>ModernChair</code> 구상클래스에 의해 구현된다</li>
</ul>
</li>
<li><strong>구상 제품</strong>: 추상 제품의 구현</li>
<li><strong>추상 팩토리</strong> 인터페이스: 각각의 추상 제품을 생성하기 위한 여러 메서들의 집합을 선언한다</li>
<li><strong>구상 팩토리</strong>들: 추상 팩토리의 생성 메서드를 구현한다<ul>
<li>각 구상 팩토리는 제품들의 특정 변형들에 해당한다 =&gt; 해당 특정 변형들만 생성한다</li>
<li>(예) <code>VictorianFactory</code>는 <code>VictorianChair</code>, <code>VictorianTable</code> 등만 생성한다</li>
</ul>
</li>
<li>구상 팩토리들은 구상 제품들을 인스턴스화하지만, 그 제품들의 생성 메서드들의 시그니처들은 그에 해당하는 추상제품들을 반환해야 한다<ul>
<li>왜냐? 그래야지 팩토리를 사용하는 클라이언트 코드가 팩토리에서 받은 제품의 특정 변형과 결합되지 않는다</li>
<li>클라이언트는 추상 인터페이스를 통해 팩토리/제품 변형의 객체들과 소통하는 한 그 어떤 구상 팩토리/제품 변형과 작업할 수 있다</li>
</ul>
</li>
</ul>
<p>용도</p>
<ul>
<li>한 제품군의 다양한 패밀리와 상호작용하되, 확장성을 위해서 각 제품의 구상 클래스에 의존하고 싶지 않을 때</li>
</ul>
<p>장점</p>
<ul>
<li>팩토리에서 생성되는 제품들의 상호 호환을 보장한다</li>
<li>구상 제품들과 클라이언트 코드 간 결합도를 낮춘다</li>
<li>단일 책임 원칙: 제품 생성 코드를 한 곳으로 추출하여 코드를 쉽게 유지보수할 수 있다</li>
<li>개방 폐쇠 원칙: 기존 클라이언트 코드를 훼손하지 않고 제품의 새로운 변형들을 생성할 수 있다</li>
</ul>
<p>단점</p>
<ul>
<li>패턴과 함께 여러 인터페이스와 구상 클래스를 도입하기 때문에 코드가 복잡해질 수 있다</li>
</ul>
<h4 id="3-빌더-패턴-builder-pattern">3. 빌더 패턴 (Builder Pattern)</h4>
<p>빌더 패턴의 구성 요소</p>
<ul>
<li><strong>빌더</strong> 인터페이스: 모든 유형의 빌더들에 공통적인 제품 생성 단계들을 선언한다</li>
<li><strong>구상 빌더</strong>: 생성 단계들의 다양한 구현을 제공한다<ul>
<li>공통 인터페이스를 따르지 않는 제품들도 생산할 수 있다 (필드 하나는 포함하지 않는다던지)</li>
</ul>
</li>
<li><strong>제품</strong>: 구상 빌더의 결과로 만들어진 객체들</li>
<li><strong>디렉터</strong> 클래스: 생성 단계들을 호출하는 순서를 정의한다<ul>
<li>필수적이지는 않다</li>
</ul>
</li>
</ul>
<p><img alt="" src="https://velog.velcdn.com/images/becooq81/post/fc5d3a0f-c5c5-4d61-b3f2-63c5b572ac42/image.png" /></p>
<p>용도</p>
<ul>
<li>점층적 생성자를 제거한다</li>
<li>일부 제품의 다른 표현들을 생성하고 싶을 때 </li>
</ul>
<blockquote>
<p>점층적 생성자란 다음과 같다</p>
</blockquote>
<pre><code class="language-java">class Pizza {
    Pizza(int size) { ... }
    Pizza(int size, boolean cheese) { ... }
    Pizza(int size, boolean cheese, boolean pepperoni) { ... }
    ...</code></pre>
<p>Spring의 <code>@Builder</code></p>
<ul>
<li>빌더 패턴이 객체의 단계적인 생성을 지원한다 </li>
<li>클래스에 대해<code>@Builder</code> 어노테이션을 선언하면 <code>Lombok</code>이 해당 클래스에 대한 빌더 클래스를 자동으로 생성한다</li>
</ul>
<pre><code class="language-java">import lombok.Builder;

@Builder
public class User {
    private String name;
    private int age;
}

...

User user = User.builder()
                .name(&quot;Alice&quot;)
                .age(30)
                .build();</code></pre>
<h3 id="행동-패턴-behavioral-pattern">행동 패턴 (Behavioral Pattern)</h3>
<p>클래스와 객체들이 상호작용하는 방법과 역할을 분담하는 방법을 다루는 패턴.</p>
<p>(ex) Template method, Singleton, Observer, State, Visitor, etc.</p>
<h4 id="1-옵저버-패턴-observer-pattern">1. 옵저버 패턴 (Observer Pattern)</h4>
<p>하나의 객체에 발생하는 모든 이벤트에 대하여 여러 객체에 이를 알리는 구독 메커니즘을 정의한다</p>
<p>옵저버 패턴의 구성 요소</p>
<ul>
<li><strong>주제(subject)</strong>: 시간에 따라 변경될 수 있는 주요한 상태를 가진 객체<ul>
<li>구독자 객체들에 대한 참조 리스트를 저장한다 (배열 등)</li>
<li>그 리스트에 구독자를 추가하거나 제거할 수 있는 <code>public</code> 메서드를 갖는다</li>
</ul>
</li>
</ul>
<p><img alt="" src="https://velog.velcdn.com/images/becooq81/post/437bfe1e-19aa-4ad4-adba-aa37761b9f66/image.png" /></p>
<p>용도</p>
<ul>
<li>event-driven 프로그래밍 (예) 메시지 알림 등</li>
<li>한 객체의 상태가 타 객체들에게 알려져야 할 때</li>
</ul>
<p>장점</p>
<ul>
<li>개방 폐쇄 원칙: 주제 객체 코드를 변경하지 않고도 새 구독자 클래스를 도입할 수 있다 <ul>
<li>구독자 클래스들은 공통 인터페이스를 구현한다고 가정한다</li>
</ul>
</li>
</ul>
<p>단점</p>
<ul>
<li>구독자는 무작위로 알림을 받는다</li>
</ul>
<h3 id="구조-패턴-structural-pattern">구조 패턴 (Structural Pattern)</h3>
<p>구조를 유연하고 효율적으로 유지하면서, 더 큰 구조로 조립하는 방법을 다루는 패턴.</p>
<p>(ex) Adapter, Proxy, Decorator, Composite, etc.</p>
<h4 id="1-데코레이터-패턴-decorator-pattern">1. 데코레이터 패턴 (Decorator Pattern)</h4>
<p>객체의 구조를 건들 필요 없이 객체에 새 행위를 추가한다. </p>
<p>장점</p>
<ul>
<li>클래스의 기능을 유연하게 확장하고 싶을 때</li>
<li>해당 클래스와 연관된 타 클래스에 영향을 주지 않으면서, 해당 클래스를 확장하고 싶을 때</li>
<li>개방 폐쇄 원칙<ul>
<li>기존 클래스는 수정되지 않는다 =&gt; 수정에 닫혀있다</li>
<li>decorator 클래스가 기능을 확장한다 =&gt; 확장에는 열려있다</li>
</ul>
</li>
<li>단일 책임 원칙: 각 데코레이터 클래스는 한 가지 기능을 추가하는 책임을 다한다<ul>
<li>각 클래스를 간단하고, 유지보수하기 용이한 형태로 유지한다</li>
</ul>
</li>
</ul>
<pre><code class="language-java">// Base component
public interface Coffee {
    String getDescription();
    double cost();
}

// Concrete component
public class BasicCoffee implements Coffee {
    public String getDescription() {
        return &quot;Basic Coffee&quot;;
    }

    public double cost() {
        return 2.0;
    }
}

// Decorator
public abstract class CoffeeDecorator implements Coffee {
    protected Coffee decoratedCoffee;

    public CoffeeDecorator(Coffee coffee) {
        this.decoratedCoffee = coffee;
    }

    public String getDescription() {
        return decoratedCoffee.getDescription();
    }

    public double cost() {
        return decoratedCoffee.cost();
    }
}

// Concrete decorators
public class MilkDecorator extends CoffeeDecorator {
    public MilkDecorator(Coffee coffee) {
        super(coffee);
    }

    public String getDescription() {
        return decoratedCoffee.getDescription() + &quot;, Milk&quot;;
    }

    public double cost() {
        return decoratedCoffee.cost() + 0.5;
    }
}

public class SugarDecorator extends CoffeeDecorator {
    public SugarDecorator(Coffee coffee) {
        super(coffee);
    }

    public String getDescription() {
        return decoratedCoffee.getDescription() + &quot;, Sugar&quot;;
    }

    public double cost() {
        return decoratedCoffee.cost() + 0.2;
    }
}

// Usage
public class CoffeeShop {
    public static void main(String[] args) {
        Coffee coffee = new BasicCoffee();
        coffee = new MilkDecorator(coffee);
        coffee = new SugarDecorator(coffee);

        System.out.println(coffee.getDescription());
        System.out.println(&quot;Total Cost: &quot; + coffee.cost());
    }
}
</code></pre>
<hr />
<p>참고</p>
<ul>
<li><a href="https://refactoring.guru/ko/design-patterns/abstract-factory">https://refactoring.guru/ko/design-patterns/abstract-factory</a></li>
<li><a href="https://refactoring.guru/ko/design-patterns/singleton">https://refactoring.guru/ko/design-patterns/singleton</a></li>
<li><a href="https://refactoring.guru/ko/design-patterns/observer">https://refactoring.guru/ko/design-patterns/observer</a></li>
<li><a href="https://www.hanbit.co.kr/channel/category/category_view.html?cms_code=CMS8616098823">https://www.hanbit.co.kr/channel/category/category_view.html?cms_code=CMS8616098823</a></li>
</ul>