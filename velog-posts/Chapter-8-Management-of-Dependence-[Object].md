<blockquote>
<p>이 문서는 &lt;오브젝트 (조영호 지음)&gt;을 읽으며 작성한 개인 노트입니다.</p>
</blockquote>
<h1 id="의존성-관리하기">의존성 관리하기</h1>
<p>잘 설계된 객체지향 애플리케이션은 작고 응집도 높은 객체들로 구성된다.</p>
<ul>
<li><strong>작고 응집도 높은 객체</strong>: 책임의 초점이 명확하고, 한 가지 일만 잘하는 객체</li>
<li>이런 작은 객체가 단독으로 수행할 수 있는 작업은 적다 =&gt; 일반적으로 애플리케이션의 기능을 구현하기 위해서는 다른 객체에 도움을 요청해야 한다. </li>
<li>이러한 요청이 객체 간 <strong>협력</strong>을 낳는다.</li>
</ul>
<p>협력은 필수적이다. 단, 과도한 협력은 설계를 곤경에 빠트릴 수 있다.</p>
<ul>
<li>협력을 하기 위해서는 다른 객체가 존재한다는 사실, 그 객체가 수신할 수 있는 메세지를 알아야 한다. </li>
<li>이 지식이 객체 간의 <strong>의존성</strong>을 낳는다</li>
</ul>
<p>협력을 위해 의존성이 필요하다. 단, 과도한 의존성은 애플리케이션을 수정하기 어렵게 만든다.</p>
<p><strong>객체지향 설계의 핵심은 협력을 위해 필요한 의존성은 유지하고, 변경을 방해하는 의존성은 제거하는 데 있다.</strong></p>
<p>이 관점에서 객체지향 설계는 객체가 변화를 받아들일 수 있게 의존성을 정리하는 기술이다</p>
<h1 id="1-의존성-이해하기">1. 의존성 이해하기</h1>
<h2 id="변경과-의존성">변경과 의존성</h2>
<p>의존성은 실행 시점과 구현 시점에 따라 다른 의미를 갖는다</p>
<ul>
<li><strong>실행 시점</strong>: 의존하는 객체가 정상적으로 동작하기 위해서는 실행 시에 의존 대상 객체가 반드시 존재해야 한다</li>
<li><strong>구현 시점</strong>: 의존 대상 객체가 변경될 경우 의존하는 객체도 함께 변경된다</li>
</ul>
<h3 id="영화-예매-시스템의-periodcondition-클래스로-의존성을-살펴보자">영화 예매 시스템의 <code>PeriodCondition</code> 클래스로 의존성을 살펴보자</h3>
<pre><code class="language-java">public class PeriodCondition implements DiscountCondition {
    private DayOfWeek dayOfWeek;
    private LocalTime startTime;
    private LocalTime endTime;

    …

    public boolean isSatisfiedBy(Screening screening) {
        return screening.getStartTime().getDayOfWeek().equals(dayOfWeek) &amp;&amp;
            startTime.compareTo(screening.getStartTime().toLocalTime()) &lt;= 0 &amp;&amp;
            endTime.compareTo(screening.getStartTime().toLocalTime()) &gt;= 0;
    }
} </code></pre>
<ul>
<li>실행 시점에 <code>PeriodCondition</code>의 인스턴스가 정상적으로 동작하기 위해서는 <code>Screening</code>의 인스턴스가 필요하다<ul>
<li><code>Screening</code>의 인스턴스가 존재하지 않거나, <code>Screening</code>이 <code>getStartTime</code> 메시지를 이해할 수 없으면 메서드가 예상대로 동작하지 않을 것이다</li>
</ul>
</li>
<li><code>Screening</code>의 변경은 <code>PeriodCondition</code>에 영향을 미치지만, 그 역은 성립하지 않는다<ul>
<li><code>PeriodCondition</code>은 <code>Screening</code>에 의존한다</li>
</ul>
</li>
</ul>
<blockquote>
</blockquote>
<ul>
<li><strong>어떤 객체가 예정된 작업을 정상적으로 수행하기 위해 다른 객체를 필요로 하는 경우, 두 객체에 의존성이 존재한다고 말한다</strong></li>
<li>의존성은 방향성을 갖는다 =&gt; <strong>단방향</strong></li>
</ul>
<p>두 요소 사이의 의존성은 의존되는 요소가 변경될 때 의존하는 요소도 함께 변경될 수 있다는 것을 의미한다. 
<strong>의존성은 변경에 의한 영향의 전파 가능성을 암시한다</strong></p>
<p>다음 그림은 <code>PeriodCondition</code>이 의존하는 모든 대상을 표현한다</p>
<p><img alt="" src="https://velog.velcdn.com/images/becooq81/post/00808b7f-9472-48a5-bfe8-be07aab29a68/image.png" /></p>
<ol>
<li><code>DayOfWeek</code>와 <code>LocalTime</code>은 <code>PeriodCondition</code>의 인스턴스 변수로 사용된다</li>
<li><code>Screening</code>은 메서드 인자로 사용된다</li>
<li><code>PeriodCondition</code>이 <code>DiscountCondition</code>에 의존하는 이유는 인터페이스에 정의된 오퍼레이션들을 퍼블릭 인터페이스의 일부로 포함시키기 위해서다</li>
</ol>
<h2 id="의존성-전이">의존성 전이</h2>
<p>의존성은 전이될 수 있다. =&gt; <strong>Transitive Dependency</strong></p>
<p>(예) <code>PeriodCondition</code>이 <code>Screening</code>에 의존할 경우 <code>PeriodCondition</code>은 <code>Screening</code>이 의존하는 대상에 대해서도 자동적으로 의존하게 된다. 즉, <code>Screening</code>이 가지는 의존성이 <code>Screening</code>에 의존하는 <code>PeriodCondition</code>으로도 전파된다. </p>
<h3 id="직접-간접-의존성">직접, 간접 의존성</h3>
<p>의존성은 함께 변경될 수 있는 가능성을 의미한다.</p>
<ul>
<li>모든 경우에 의존성이 전이되지는 않는다. </li>
<li>실제 전이 여부는 변경의 방향과 캡슐화의 정도에 따라 달라진다</li>
</ul>
<p>의존성은 직접 의존성과 간접 의존성으로 나뉠 수 있다</p>
<ul>
<li><strong>직접 의존성</strong>: 한 요소가 다른 요소에 직접 의존하는 경우 <ul>
<li>(예) <code>PeriodCondition</code>이 <code>Screening</code>에 의존한다 =&gt; 코드에 명시적으로 드러난다</li>
</ul>
</li>
<li><strong>간접 의존성</strong>:  직접적인 관계는 존재하지 않지만 의존성 전이에 의해 영향이 전파되는 경우<ul>
<li>명시적으로 드러나지는 않는다</li>
</ul>
</li>
</ul>
<h2 id="런타임-의존성과-컴파일타임-의존성">런타임 의존성과 컴파일타임 의존성</h2>
<ul>
<li><strong>런타임</strong>: 애플리케이션이 실행되는 시점</li>
<li><strong>컴파일타임</strong>: 작성된 코드를 컴파일하는 시점<ul>
<li>의미가 미묘하다<ul>
<li>문맥에 따라서는 코드 그 자체를 가르키기도 한다</li>
<li>시간보다는 코드의 구조가 더 중시된다</li>
<li>동적 타입 언어는 컴파일 타임이 존재하지 않는다</li>
</ul>
</li>
</ul>
</li>
</ul>
<p>객체지향 애플리케이션에서 런타임의 주인공은 객체다. <strong>런타임 의존성이 다루는 주제는 객체 사이의 의존성이다.</strong></p>
<p>코드 관점에서 주인공은 클래스다. <strong>컴파일타임 의존성이 다루는 주제는 클래스 사이의 의존성이다.</strong></p>
<p>즉, 런타임 의존성과 컴파일타임 의존성이 다를 수 있다. 
유연하고 재사용 가능한 코드를 설계하기 위해서는 두 종류의 의존성을 서로 다르게 만들어야 한다</p>
<h3 id="영화-예매-시스템">영화 예매 시스템</h3>
<p><code>Movie</code>는 가격을 계산하기 위해 비율 할인 정책과 금액 할인 정책을 모두 적용할 수 있게 설계해야 한다</p>
<p><img alt="" src="https://velog.velcdn.com/images/becooq81/post/df9f5636-a7b6-4f8f-b8e3-e45c70da385b/image.png" /></p>
<h4 id="코드-관점에서의-의존성">코드 관점에서의 의존성</h4>
<p>그래서 <code>AmountDiscountPolicy</code>와 <code>PercentDiscountPolicy</code>가 추상 클래스 <code>DicsountPolicy</code>를 상속받게 한 후, <code>Movie</code>가 이 추상 클래스에 의존하도록 클래스 관계를 설계한다. </p>
<p>이로써 <code>Movie</code>는 <code>AmountDiscountPolicy</code>와 <code>PercentDiscountPolicy</code>에 대해 의존성을 갖지 않는다. 오직 추상 클래스에만 의존한다. 단, 이는 코드 관점의 이야기다.</p>
<h4 id="런타임-의존성">런타임 의존성</h4>
<ul>
<li><code>Movie</code>가 금액 할인 정책을 적용하기 위해서는 <code>AmountDiscountPolicy</code>와 협력해야 한다<ul>
<li>비율 할인 정책을 적용하기 위해서는 <code>PercentDiscountPolicy</code>와 협력해야 한다</li>
</ul>
</li>
<li>실행 시점의 <code>Movie</code> 인스턴스는 각 정책 인스턴스와 협력할 수 있어야 한다 </li>
</ul>
<h4 id="코드-작성-시점의-movie-클래스는-할인-정책을-구현한-두-클래스의-존재를-모르지만-실행-시점의-movie-객체는-두-클래스의-인스턴스와-협력할-수-있다">코드 작성 시점의 <code>Movie</code> 클래스는 할인 정책을 구현한 두 클래스의 존재를 모르지만, 실행 시점의 Movie 객체는 두 클래스의 인스턴스와 협력할 수 있다</h4>
<p>유연하고 재사용 가능한 설계를 창조하기 위해서는 동일한 소스코드 구조를 갖고 다양한 실행 구조를 만들 수 있어야 한다</p>
<h2 id="컨텍스트-독립성">컨텍스트 독립성</h2>
<p>클래스는 자신과 협력할 객체의 구체적인 클래스에 대해 알아서는 안 된다.
구체적인 클래스를 알면 알수록 그 클래스가 사용되는 특정한 문맥에 강하게 결합되기 때문이다.</p>
<blockquote>
<p>구체 클래스에 대해 의존하는 것은 클래스의 인스턴스가 어떤 문맥에서 사용될지 명시하는 것과 같다.
(예) <code>Movie</code> 클래스 안에 <code>PercentDiscountPolicy</code> 클래스에 대한 컴파일타임 의존성을 명시하면, <code>Movie</code>가 비율 할인 정책에 적용된 영화의 요금을 계산하는 문맥에서 사용될 것이라는 것을 가정하는 것이다. 
(예) <code>Movie</code> 클래스에 추상클래스 <code>DiscountPolicy</code>에 대한 컴파일타임 의존성을 명시하면 구체적인 문맥을 정의하지 않는다. </p>
</blockquote>
<p>클래스가 특정 문맥에 강하게 결합될수록 다른 문맥에서 사용하기 어려워진다.</p>
<p><strong>컨텍스트 독립성</strong>: 클래스가 사용될 특정한 문맥에 대해 최소한의 가정만으로 이뤄져 있다면, 다른 문맥에서 재사용하기 더 수월하다.</p>
<h2 id="의존성-해결하기">의존성 해결하기</h2>
<p>컴파일타임 의존성은 구체적인 런타임 의존성으로 대체돼야 한다.</p>
<p><code>Movie</code> 클래스가 <code>DiscountPolicy</code> 클래스에 의존하는 <strong>컴파일타임 의존성</strong>은 런타임에는 <code>PercentDiscountPolicy</code> 또는 <code>AmountDiscountPolicy</code>에 대한 의존성으로 교체돼야 한다. </p>
<p><strong>의존성 해결</strong>: 컴파일타임 의존성을 실행 컨텍스트에 적절한 런타임 의존성으로 교체하는 것</p>
<ol>
<li>객체를 생성하는 시점에 생성자를 통해 의존성 해결</li>
</ol>
<pre><code class="language-java">public class Movie {
    public Movie(String title, Duration runningTime, Money fee, DiscountPolicy discountPolicy) {
        …
        this.discountPolicy = discountPolicy;
    }
}

…

Movie avatar = new  Movie(&quot;아바타&quot;,
    Duration.ofMinutes(120),
    Money.wons(10000),
    new AmountDiscountPolicy(...));</code></pre>
<ol start="2">
<li>객체 생성 후 <code>setter</code> 메서드로 의존성 해결</li>
</ol>
<pre><code class="language-java">public class Movie {
    public void setDiscountPolicy (DiscountPolicy discountPolicy) {
        this.discountPolicy = discountPolicy;
    }
}
…

Movie avatar = new Movie(...));
avatar.setDiscountPolicynew AmountDiscountPolicy(...));
…
avatar.setDiscountPolicynew PercentDiscountPolicy(...));</code></pre>
<p><code>setter</code> 메서드는 객체를 생성한 이후에도 의존하고 있는 대상을 변경할 수 있는 가능성을 열어 놓고 싶은 경우에 유용하다. =&gt; 유연하다
단, 객체가 생성된 후에 협력에 필요한 의존 대상을 설정하기 때문에 이 전까지는 객체의 상태가 불완전할 수 있고, 예외 발생으로 이어질 수 있다.</p>
<blockquote>
<p>생성자 방식과 <code>setter</code> 방식을 혼합한다면? 객체 생성 시점에 완전한 상태의 객체를 생성하고, 필요에 따라 의존 대상을 변경할 수 있다</p>
</blockquote>
<ol start="3">
<li>메서드 실행 시 인자를 이용해 의존성 해결</li>
</ol>
<pre><code class="language-java">public class Movie {
    public Money calculateMovieFee(Screening screening, DiscountPolicy discountPolicy) {
        return fee.minus(discountPolicy.calculateDiscountAmount(screening));
    }
} </code></pre>
<p><code>Movie</code>가 항상 할인 정책을 알 필요까지는 없고, 가격을 계산할 때만 일시적으로 알아도 무방하다면!</p>
<p>즉, 메서드 실행 동안만 일시적으로 의존 관계가 존재해도 무방하거나, 메서드가 실행될 때마다 의존 대상이 매번 달라져야 하는 경우 사용한다. </p>
<h1 id="2-유연한-설계">2. 유연한 설계</h1>
<h2 id="의존성과-결합도">의존성과 결합도</h2>
<p>객체들이 협력하기 위해서는 서로의 존재와 수행 가능한 책임을 알아야 한다. 이런 지식이 객체 간 의존성을 낳는다. 이 의존성이 과하면 문제가 될 수 있다. </p>
<h3 id="movie가-비율-할인-정책을-구현하는-percentdiscountpolicy에-직접-의존한다고-가정해보자"><code>Movie</code>가 비율 할인 정책을 구현하는 <code>PercentDiscountPolicy</code>에 직접 의존한다고 가정해보자.</h3>
<pre><code class="language-java">public class Movie {
    …
    private PercentDiscountPolicy percentDiscountPolicy;

    public MovieString title, Duration runningTime, Money fee,
        PercentDiscountPolicy percentDiscountPolicy) {
        …
        this.percentDiscountPolicy = percentDiscountPolicy;
    }

    public Money calculateMovieFee(Screening screening) {
        return fee.minus(percentDiscountPolicy.calculateDiscountAmount(screening));
    }
}</code></pre>
<p>이 코드에서는 <code>Movie</code>가 <code>PercentDiscountPolicy</code>에 명시적으로, 코드 관점에서 의존한다. 이 의존성의 존재는 괜찮지만, 의존성의 정도가 문제가 된다. </p>
<p><code>Movie</code>가 <code>PercentDiscountPolicy</code>라는 구체적인 클래스에 의존하기 때문에 다른 종류의 할인 정책이 필요한 문맥에서 <code>Movie</code>를 재사용할 수 없게 되었다. </p>
<p><code>Movie</code>가 협력하고 싶은 대상이 반드시 <code>PercentDiscountPolicy</code>의 인스턴스일 필요 없다. 협력할 객체의 클래스를 고정할 핑료가 없다. 
그래서 추상 클래스인 <code>DiscountPolicy</code>는 <code>calculateDiscountAmount</code> 메시지를 이해할 수 있는 타입을 정의함으로써 이 문제를 해결한다</p>
<h3 id="바람직한-의존성은-재사용성과-관련있다">바람직한 의존성은 재사용성과 관련있다.</h3>
<ul>
<li>어떤 의존성이 다양한 환경에서 재사용할 수 있다면 그 의존성은 바람직한 것이다. </li>
<li>어떤 의존성이 다양한 환경에서 클래스를 재사용할 수 없도록 제한한다면 그 의존성은 바람직하지 못한 것이다. </li>
<li>컨텍스트에 독립적인 의존성은 바람직하다. 특정 컨텍스트에 강하게 결합된 의존성은 바람직하지 않다. </li>
</ul>
<p><strong>결합도</strong></p>
<ul>
<li>느슨한 결합도: 어떤 두 요소 사이에 존재하는 의존성이 바람직할 때 두 요소가 느슨한/약한 결합도(loose coupling)을 갖는다</li>
<li>단단한 결합도: 어떤 두 요소 사이의 의존성이 바람직하지 못할 때 단단한/강한(tight coupling)을 갖는다</li>
</ul>
<blockquote>
<p><strong>의존성과 결합도</strong>
의존성과 결합도는 서로 다른 관점에서 관계의 특성을 설명한다. </p>
</blockquote>
<ul>
<li>의존성: 두 요소 사이의 관계 유무 <ul>
<li>의존성이 존재한다, 존재하지 않는다</li>
</ul>
</li>
<li>결합도: 두 요소 사이에 존재하는 의존성의 정도를 상대적으로 표현한다<ul>
<li>결합도가 강하다, 느슨하다</li>
</ul>
</li>
</ul>
<h2 id="지식이-결합을-낳는다">지식이 결합을 낳는다</h2>
<p><code>Movie</code>가 <code>PercentDiscountPolicy</code>에 의존하면 결합도가 높다고 한다.
<code>Movie</code>가 <code>DiscountPolicy</code>에 의존하면 결합도가 낮다고 한다.</p>
<p>=&gt; 결합도의 정도는 한 요소가 자신이 의존하고 있는 다른 요소에 대해 알고 있는 정보의 양으로 결정된다. 더 적게 알수록 두 요소는 약하게 결합된다. </p>
<p>더 많이 알고 있다는 것은 더 적은 컨텍스트에서 재사용 가능하다는 것을 의미한다. 기존 지식에 어울리지 않는 컨텍스트에서 클래스의 인스턴스를 사용하기 위해서 할 수 있는 유일한 방법은 클래스를 수정하는 것 뿐이다. </p>
<h2 id="추상화에-의존하라">추상화에 의존하라</h2>
<p><strong>추상화</strong>: 어떤 양상, 세부사항, 구조를 좀 더 명확하게 이해하기 위해 특정 절차/물체를 의도적으로 생략하거나 감춰서 복잡도를 극복한다.</p>
<p>따라서 대상에 대해 알아야 하는 지식의 양을 줄일 수 있다 =&gt; 결합도를 느슨하게 유지할 수 있다</p>
<p>일반적으로 추상화와 결합도의 관점에서 의존 대상을 다음과 같이 구분한다. 클라이언트가 알아야 하는 지식의 양이 많은 순이다. </p>
<ul>
<li>구체 클래스 의존성(concrete class dependency)</li>
<li>추상 클래스 의존성(abstract class dependency)</li>
</ul>
<p>구체 클래스에 비해 추상 클래스는 메서드의 내부 구현과 자식 클래스의 종류에 대한 지식을 클라이언트로부터 숨길 수 있다.
클라이언트가 알아야 하는 지식의 양이 더 적기 때문에 추상 클래스에 의존하는 것이 결합도가 더 낮다. </p>
<p>단, 여전히 협력하는 대상이 속한 클래스 상속 계층이 무엇인지에 대해서는 알고 있어야 한다. </p>
<ul>
<li>인터페이스 의존성(interface dependency)</li>
</ul>
<p>인터페이스에 의존하면 상속 계층을 모르더라도 협력이 가능해진다. 
협력하는 객체가 어떤 메시지를 수신할 수 있는지에 대한 지식만을 남기기 때문에 결합도가 더 낮다. </p>
<p><strong>실행 컨텍스트에 대해 알아야 하는 정보를 줄일수록 결합도가 낮아진다.</strong></p>
<h2 id="명시적인-의존성">명시적인 의존성</h2>
<pre><code class="language-java">public class Movie {
    …
    private DiscountPolicy discountPolicy;

    public Movie(String title, Duration runningTime, Money fee) {
        …
        this.discountPolicy = new AmountDiscountPolicy(…);
    }
}</code></pre>
<p>이 코드는 <code>Movie</code>클래스의 인스턴스 변수인 <code>discountPolicy</code>는 추상 클래스인 <code>DiscountPolicy</code> 타입으로 선언했지만, 생성자 내부에서 구체 클래스로 생성해서 대입한다. 따라서, 구체 클래스에 의존하게 된다. </p>
<p>결합도를 느슨하게 하기 위해서는</p>
<ol>
<li>인스턴스 변수의 타입을 추상 클래스/인터페이스로 선언하고,</li>
<li>앞서 이야기한 생성자, <code>setter</code> 메서드, 메서드 인자 방식으로 의존성을 해결해야 한다.</li>
</ol>
<p>다음과 같이 생성자 방식으로 의존성을 해결할 수 있다. </p>
<pre><code class="language-java">public class Movie {
    private DiscountPolicy discountPolicy;

    public Movie(String title, Duration runningTime, Money fee, DiscountPolicy discountPolicy) {
        …
        this.discountPolicy = discountPolicy;
    }
}</code></pre>
<p>생성자, <code>setter</code> 메서드, 메서드 인자 방식으로 의존성을 해결하면 <strong>의존성을 명시적으로 퍼블릭 인터페이스에 노출</strong>하게 된다. 이는 <strong>명시적 의존성</strong>이다.</p>
<p>반면, <code>Movie</code> 내부에서 <code>AmountDiscountPolicy</code>의 인스턴스를 직접 생성하면 의존 사실을 감추기 때문에 <strong>숨겨진 의존성</strong>이라 한다. 숨겨진 의존성은 이를 파악하기 위해 클래스 내부 구현을 직접 살펴야 하기 때문에 까다롭다. </p>
<p>숨겨진 의존성의 단점</p>
<ul>
<li>의존성을 파악하기 위해 클래스 내부 구현을 살펴봐야 한다</li>
<li>클래스를 다른 컨텍스트에서 재사용하기 위해 내부 구현을 변경해야 한다</li>
</ul>
<p>*<em>그래서 의존성은 퍼블릭 인터페이스를 통해 명시적으로 표현돼야 한다. *</em></p>
<p>명시적인 의존성을 사용해야만 퍼블릭 인터페이스를 통해 컴파일타임 의존성을 적절한 런타임 의존성으로 교체할 수 있다. </p>
<p><strong>경계해야 하는 것은 의존성 자체가 아니라 의존성을 감추는 것이다.</strong></p>
<h2 id="new는-해롭다">new는 해롭다</h2>
<p>클래스의 인스턴스를 생성하는 <code>new</code>를 잘못 사용하면 클래스 사이의 결합도가 극단적으로 높아진다. </p>
<ol>
<li><code>new</code> 연산자를 사용하기 위해서는 구체 클래스의 이름을 직접 기술해야 한다. 따라서 추상화가 아닌 구체 클래스에 의존할 수 밖에 없다</li>
<li><code>new</code> 연산자는 생성하려는 구체 클래스 뿐만 아니라 어떤 인자를 이용해 클래스의 생성자를 호출해야 하는지도 알아야 한다. 클라이언트가 알아야 하는 지식의 양이 늘어난다 =&gt; 결합도가 높아진다.</li>
</ol>
<h3 id="영화-예시">영화 예시</h3>
<pre><code class="language-java">public class Movie {
    private DiscountPolicy discountPolicy;

    public Movie(String title, Duration runningTime, Money fee) {
        this.discountPolicy = new AmountDiscountPolicy (Money. wons(800),
                    new SequenceCondition (1),
                    new SequenceCondition (10),
                    new PeriodCondition(DayOfWeek. MONDAY,
                                LocalTime.of(10, 0), LocalTime.of(11, 59)),
                                new PeriodCondition(DayOfWeek.THURSDAY,
                                LocalTime.of(10, 0), LocalTime.of(20, 59))
                    )
        );
    }
}</code></pre>
<p>위와 같이 <code>Movie</code> 클래스가 <code>AmountDiscountPolicy</code> 인스턴스를 생성하기 위해서는 생성자에 전달되는 인자를 알아야 한다. 심지어 <code>AmountDiscountPolicy</code>가 참조하는 두 구체 클래스 (<code>SequenceCondition</code>, <code>PeriodCondition</code>)에도 의존하게 된다. </p>
<p>결합도가 높으면 변경에 의해 영향을 받기 쉬워진다. </p>
<p><img alt="" src="https://velog.velcdn.com/images/becooq81/post/38890fe9-6315-4c39-a96d-ea6607741523/image.png" /></p>
<p><code>new</code>는 클래스를 구체 클래스에 결합시킬 뿐만 아니라, 협력할 클래스의 인스턴스를 생성하기 위해 어떤 인자들이, 어떤 순서로 사용되어야 하는지, 인자로 사용되는 구체 클래스에 대한 의존성까지 추가한다. </p>
<h4 id="인스턴스를-생성하는-로직과-사용하는-로직을-분리하자">인스턴스를 생성하는 로직과 사용하는 로직을 분리하자</h4>
<p><code>AmountDiscountPolicy</code>를 사용하는 <code>Movie</code>는 그 인스턴스를 생성해서는 안된다. 해당하는 인스턴스를 사용하기만 하기 위해서 외부로부터 이미 생성된 <code>AmountDiscountPolicy</code>의 인스턴스를 전달받아야 한다. </p>
<p>이는 의존성 해결 방법과 동일하다. </p>
<pre><code class="language-java">public class Movie {
    private DiscountPolicy discountPolicy;
    public Movie(String title, Duration runningTime, Money fee, DiscountPolicy discountPolicy) {
        …
        this.discountPolicy = discountPolicy;
    }
}</code></pre>
<p>이로써 <code>DiscountPolicy</code>를 생성하는 로직(클라이언트)과 사용하는 로직 (<code>Movie</code>)를 분리할 수 있다. 이제 <code>Movie</code>는 <code>DiscountPolicy</code>를 상속하는 모든 자식 클래스와 협력할 수 있게 된다. </p>
<h2 id="가끔은-생성해도-무방하다">가끔은 생성해도 무방하다</h2>
<p>클래스 안에서 객체의 인스턴스를 직접 생성하는 방식이 유용한 경우도 있다.
(예) 협력하는 기본 객체를 설정하고 싶은 경우
(예2) <code>Movie</code>가 대부분의 경우에는 <code>AmountDiscountPolicy</code>의 인스턴스와 협력하고, 가끔씩만 <code>PercentDiscountPolicy</code>의 인스턴스와 협력하는 경우에는 인스턴스 생성 책임을 완전히 클라이언트로 옮기면 클라이언트 간 중복 코드가 늘어난다.</p>
<p><strong>해결방법</strong>: 기본 객체를 생성하는 생성자를 추가하고, 이 생성자에서 <code>DiscountPolicy</code>의 인스턴스를 인자로 받는 생성자를 체이닝한다.</p>
<pre><code class="language-java">public class Movie {
    private DiscountPolicy discountPolicy;

    public Movie(String title, Duration runningTime, Money fee) {
        this(title, runningTime, fee, new AmountDiscountPolicy(…));
    }

    public Movie(String title, Duration runningTime, Money fee, DiscountPolicy discountPolicy) {
        …
        this.discountPolicy = discountPolicy;
    }
}</code></pre>
<p>추가된 생성자 안에서 기존 생성자를 호출하여 <code>AmountDiscountPolicy</code> 클래스의 인스턴스를 생성한다. 이렇게 생성자가 체인처럼 연결된다.</p>
<p>이제 클라이언트는 대부분의 경우에 추가된 간략한 생성자로 <code>AmountDiscountPolicy</code>의 인스턴스와 협력하면서도, 컨텍스트에 적절한 <code>DiscountPolicy</code>의 인스턴스로 의존성을 교체할 수 있다.</p>
<p>메서드 오버로딩의 경우에도 사용할 수 있다. </p>
<pre><code class="language-java">public class Movie {
    public Money calculateMovieFee(Screening screening) {
        return calculateMovieFee(screening, new AmountDiscountPolicy(…)));
    }

    public Money calculateMovieFee(Screening screening,
            DiscountPolicy discountPolicy) {
        return fee.minus(discountPolicy.calculateDiscountAmount(screening));
    }
}</code></pre>
<h4 id="설계는-트레이드오프-활동이다">설계는 트레이드오프 활동이다.</h4>
<p>여기서는 트레이드오프의 대상은 결합도와 사용성이다. </p>
<p>구체클래스에 의존하더라도 클래스의 사용성이 더 중요하다면 결합도를 높이는 방향으로 코드를 작성할 수 있다.</p>
<p>그럼에도 가급적 구체 클래스에 대한 의존성을 제거할 수 있는 방법을 찾는 것이 좋다. 종종 모든 결합도가 모이는 새로운 클래스를 추가해서 사용성과 유연성 두 마리 토끼를 잡을 수도 있다.</p>
<h2 id="표준-클래스에-대한-의존은-해롭지-않다">표준 클래스에 대한 의존은 해롭지 않다.</h2>
<p>의존성은 변경에 대한 영향을 암시하기 때문에 불편한 것이다. 따라서 변경될 확률이 거의 없는 클래스라면 의존성이 문제가 되지 않는다. 
(예) Java에서는 JDK에 포함되는 표준 클래스 </p>
<p><code>ArrayList</code> 클래스는 수정될 가능성이 매우 낮기 때문에 인스턴스를 직접 생성해도 문제가 되지 않는다.</p>
<pre><code class="language-java">public abstract class DiscountPolicy {
    private List&lt;DiscountCondition&gt; conditions = new ArrayList&lt;&gt;();
}</code></pre>
<p>클래스를 직접 생성하더라도 가능한 한 추상적인 타입으로 선언하는 것이 확장성 측면에서 유리하다. 이렇게 다양한 <code>List</code> 타입 객체로 이 인스턴스 변수를 대체할 수 있고, 설계의 유연성을 높일 수 있다. </p>
<h2 id="컨텍스트-확장하기">컨텍스트 확장하기</h2>
<p>이제 실제로 <code>Movie</code>가 유연하다는 사실을 입증하기 위해 다른 컨텍스트에서 <code>Movie</code>를 확장해서 재사용하는 두 가지 예를 살펴보자. </p>
<h3 id="1-할인-혜택을-제공하지-않는-영화의-예매-요금을-계산한다">1. 할인 혜택을 제공하지 않는 영화의 예매 요금을 계산한다</h3>
<h4 id="1-1-discountpolicy에-어떠한-객체도-할당하지-않는다">1-1. discountPolicy에 어떠한 객체도 할당하지 않는다.</h4>
<pre><code class="language-java">public class Movie {

    public Movie(String title, Duration runningTime, Money fee) {
        this(title, runningTime, fee, null);
    }

    public Movie(String title, Duration runningTime, Money fee, DiscountPolicy discountPolicy) {
        …
        this.discountPolicy = discountPolicy;
    }

    public Money calculateMovieFee(Screening screening) {
        if (discountPolicy = null) {
            return fee;
        }
        return fee.minus(discountPolicy.calculateDiscountAmount(screening));
    }
}</code></pre>
<p>앞서 설명한 생성자 체이닝 기법으로 기본값으로 <code>null</code>을 할당하고, <code>discountPolicy</code>의  값이 <code>null</code>이면 할인 정책을 적용하지 않는다.</p>
<p>이 코드는 동작하기는 하지만, 여태 <code>Movie</code>와 <code>DiscountPolicy</code> 간 협력 방식에 예외를 만든다. 그리고 이 예외 케이스를 처리하기 위해 <code>Movie</code>의 내부 코드를 직접 수정해야 하며, 버그 발생 가능성을 높인다. </p>
<h4 id="1-2-기존에-movie와-discountpolicy가-협력하던-방식을-따른다">1-2. 기존에 <code>Movie</code>와 <code>DiscountPolicy</code>가 협력하던 방식을 따른다</h4>
<p>할인 정책이 존재하지 않는다는 사실을 할인 정책의 한 종류로 정의한다. 
=&gt; <code>DiscountPolicy</code>를 상속하고, 할인할 금액으로 0원을 반환하는 <code>NoneDiscountPolicy</code> 클래스를 추가한다. </p>
<pre><code class="language-java">public class NoneDiscountPolicy extends DiscountPolicy {

    @Override
    protected Money getDiscountAmount(Screening Screening) {
        return Money.ZERO;
    }

}</code></pre>
<p>이제 <code>Movie</code> 클래스의 코드 수정 없이 할인 혜택을 제공하지 않는 영화를 구현할 수 있다.</p>
<h3 id="2-중복-적용이-가능한-할인-정책을-구현한다">2. 중복 적용이 가능한 할인 정책을 구현한다</h3>
<p>중복 할인: 금액 할인 정책과 비율 할인 정책을 혼합해서 적용할 수 있는 할인 정책</p>
<p>할인 정책을 중복 적용하기 위해서는 <code>Movie</code>가 하나 이상의 <code>DiscountPolicy</code>와 협력할 수 있어야 한다.</p>
<h4 id="2-1-movie가-discountpolicy의-인스턴스들로-구성된-list를-인스턴스-변수로-정의한다">2-1. <code>Movie</code>가 <code>DiscountPolicy</code>의 인스턴스들로 구성된 <code>List</code>를 인스턴스 변수로 정의한다</h4>
<p>하지만, 중복 할인 정책을 구현하기 위해 기존의 할인 정책의 협력 방식과는 다른 예외 케이스를 만든다.</p>
<h4 id="2-2-중복-할인-정책을-할인-정책의-종류로-정의한다">2-2. 중복 할인 정책을 할인 정책의 종류로 정의한다.</h4>
<p><code>DiscountPolicy</code>를 상속하고, 중복 할인 정책을 구현하는 <code>OverlappedDiscountPolicy</code>를 만든다.</p>
<pre><code class="language-java">public class OverlappedDiscountPolicy extends DiscountPolicy {

    private List&lt;DiscountPolicy&gt; discountPolicies = new ArrayList&lt;&gt;();

    public OverlappedDiscountPolicy(DiscountPolicy . . . discountPolicies) {
        this. discountPolicies = Arrays.asList(discountPolicies);
    }

    @Override
    protected Money getDiscountAmount (Screening screening) {
        Money result = Money.ZERO;
        for (DiscountPolicy each : discountPolicies) {
            result = result.plus(each.calculateDiscountAmount(screening));
        }
        return result;
    }
}</code></pre>
<p>이 방식으로는 <code>OverlappedDiscountPolicy</code>의 인스턴스를 생성해서 <code>Movie</code> 클래스에 전달만 해도 중복 할인을 쉽게 적용할 수 있다. </p>
<h3 id="movie가-협력해야-하는-객체를-변경하는-것만으로도-movie를-새로운-컨텍스트에서-재사용할-수-있기-때문에-movie는-유연하고-재사용-가능하다"><code>Movie</code>가 협력해야 하는 객체를 변경하는 것만으로도 <code>Movie</code>를 새로운 컨텍스트에서 재사용할 수 있기 때문에 <code>Movie</code>는 유연하고 재사용 가능하다.</h3>
<ol>
<li><code>Movie</code>가 <code>DiscountPolicy</code>라는 추상화에 의존한다.</li>
<li>생성자를 통해 <code>DiscountPolicy</code>에 대한 의존성을 명시적으로 드러낸다.</li>
<li><code>new</code>와 같이 구체 클래스를 직접적으로 다뤄야 하는 책임을 <code>Movie</code> 외부로 옮겼다.</li>
<li><code>Movie</code>가 의존하는 추상화인 <code>DiscountPolicy</code> 클래스에 자식 클래스를 추가함으로써 간단하게 <code>Movie</code>가 사용될 컨텍스트를 확장할 수 있었다.</li>
</ol>
<h2 id="조합-가능한-행동">조합 가능한 행동</h2>
<p>어떤 객체와 협력하느냐에 따라 객체의 행동이 달라지는 것은 유연하고 재사용 가능한 설계가 가진 특징이다.</p>
<p>유연하고 재사용 가능한 설계는 응집도 높은 책임들을 가진 작은 객체들을 다양한 방식으로 연결함으로써 애플리케이션의 기능을 쉽게 확장할 수 있다. </p>
<p>객체가 어떻게(how) 하는지를 장황하게 나열하지 않고도 객체들의 조합을 통해 무엇(what)을 하는지를 표현하는 클래스들로 구성된다. 
즉, 코드에 드러난 로직을 해석할 필요 없이, 객체가 어떤 객체와 연결됐는지를 보는 것만으로도 객체의 행동을 쉽게 예상하고 이해할 수 있다. 선언적으로 객체의 행도응ㄹ 정의할 수 있다. </p>
<p><strong>훌륭한 객체지향 설계란 객체가 어떻게 하는지를 표현하는 것이 아니라 객체들의 조합을 선언적으로 표현함으로써 객체들이 무엇을 하는지를 표현하는 설계다.</strong></p>
<p>이런 설계를 창조하는 데 있어서 핵심은 의존성을 관리하는 것이다.</p>