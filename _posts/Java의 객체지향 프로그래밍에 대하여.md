<h1 id="java는-객체지향-언어다">Java는 객체지향 언어다.</h1>
<p>Java는 객체지향 언어다. 그럼 객체 지향은 무엇인가? Java는 객체 지향을 어떻게 구현하는가? 왜 구현하는가?</p>
<h1 id="객체-object">객체 (Object)</h1>
<p>객체지향 프로그래밍을 이해하려면 클래스(Class)와 객체(Object)가 무엇인지부터 생각해봐야 한다.</p>
<p>객체의 블루프린트, 즉 설계도가 바로 클래스다. 클래스는 멤버 변수(속성)와 메서드(행위)를 통해 하나의 타입을 정의한다. 예를 들자면, <code>Car</code> 클래스는 차의 설계도를 정의하는 것이다. <code>Car</code> 클래스의 멤버 변수인 차종과 위치는 차의 속성을 표현하고, 메서드인 <code>drive</code>(운전)은 차의 행위를 표현해서 차라는 사물의 종류를 정의한다. </p>
<p>클래스라는 설계도를 기반하여 개별 사물을 생성하는 것이 객체다. 차를 설계했으면 차를 만들어서 운전을 해야 하는 것처럼, 클래스를 정의했으면 객체를 생성해서 활용해야 한다. </p>
<blockquote>
<p>객체와 클래스 간 개념을 이해하기 위한 예시로, 이 예시에 반하는 개념인 <code>static</code>는 추후에 첨언한다 </p>
</blockquote>
<p>객체는 객체지향 프로그래밍의 가장 기본이 되는 단위로, 실제 사물을 표현한다. 클래스를 기반으로 생성하기 때문에 특정 사물이 복잡한 상태 또는 행위를 가진다 하더라도 매번 사물을 정의할 필요 없이, 이미 정의 해둔 클래스로 생성하면 된다. </p>
<hr />
<p>처음 들으면 어떻게 구현해야 할지 조금 막막할 수도 있는 개념이다. 그래서 알아야 하는 것이 객체지향의 4가지 주요 개념인 상속, 캡슐화, 상속, 그리고 다형성이다. </p>
<ul>
<li><p>클래스의 내부 데이터를 외부의 수정 또는 접근으로부터 보호하는 것이 <strong>캡슐화(Encapsulation)</strong>다.</p>
</li>
<li><p>이미 정의 해둔 클래스를 확장하거나 부분적으로 수정(메서드 오버라이딩)해서 코드를 재사용하고, 활용하는 것이 <strong>상속(Inheritance)</strong>이다.</p>
</li>
<li><p>클래스가 복잡할 수 있어도, 객체를 사용하는 사람은 클래스 내부의 복잡함을 모르고도 간편하게 사용할 수 있도록 제공하는 것이 <strong>추상화(Abstraction)</strong>다.</p>
</li>
<li><p>하나의 객체가 여러 타입을 가질 수 있어 활용도를 높이는 것이 <strong>다형성(Polymorphism)</strong>이다.</p>
</li>
</ul>
<hr />
<p>하나씩 차근차근 알아보면 생각보다 단순한 개념들이다.</p>
<h1 id="캡슐화-encapsulation">캡슐화, Encapsulation</h1>
<p>캡슐화는 클래스 내부의 멤버에 접근을 구분해서 내부 데이터가 오염되지 않도록 방지하고, 외부에서 필요한 기능 등은 접근할 수 있도록 허용한다. </p>
<h4 id="접근-제어자">접근 제어자</h4>
<p>접근 제어자에는 <code>private</code>, <code>default</code>, <code>protected</code>, <code>public</code>이 존재한다. 접근 허용 범위 오름차순 순이다.</p>
<ul>
<li><code>private</code>은 동일 클래스 내부에서의 접근만 가능하여, 가장 좁은 범위를 허용한다.</li>
<li><code>default</code>은 접근 제어자를 사용하지 않음을 의미하며, 동일 클래스 내부와 동일 패키지 내부에서만 접근이 가능하다.</li>
<li><code>protected</code>는 동일 클래스 내부, 동일 패키지 내부, 그리고 해당 클래스를 상속하는 자식 클래스까지 접근을 허용한다.</li>
<li><code>public</code>은 모든 접근을 허용한다. </li>
</ul>
<p>클래스의 필드는 주로 <code>private</code>으로 선언해서 데이터 오염을 방지하고, 해당 필드를 조회하거나 조작할 수 있는 <code>getter</code>, <code>setter</code>와 같은 메서드를 <code>public</code>으로 정의해서 클래스 외부에서 접근은 가능하도록 허용한다. </p>
<blockquote>
<p>모든 필드에 대해 <code>setter</code>를 정의한다면 필드를 <code>private</code>으로 선언하는 의미가 없지 않겠는가? 로직을 구현하는데 필수적인 경우에만 <code>public</code>한 <code>setter</code>를 정의하는 것을 습관화하자</p>
</blockquote>
<p>결론적으로 접근제어자, 그리고 캡슐화의 장점은 다음과 같다</p>
<ol>
<li>주요한 데이터는 외부로부터 숨길 수 있다.</li>
<li>요구사항에 따라 클래스의 변수에 대해 조회만 가능하도록, 또는 조작만 가능하도록, 모두 가능하도록 등 결정할 수 있다.</li>
</ol>
<p>접근제어자는 이제부터 알아볼 상속, 추상화 등에도 필수적인 개념이다.</p>
<hr />
<h1 id="상속-inheritance">상속, Inheritance</h1>
<p>클래스 B가 클래스 A를 상속하면 클래스 A를 부모 클래스, 클래스 B를 자식 클래스(서브 클래스)라고 부른다.</p>
<p>부모 클래스는 영어로 superclass, base class, 또는 parent class라고 불린다. 자식 클래스는 영어로 subclass, derived class, extended class, 또는 child class라고 불린다.</p>
<p>자식 클래스는 부모 클래스의 모든 <code>public</code>과 <code>protected</code> 멤버(필드, 메서드, 중첩 클래스)를 상속받아 활용할 수 있어서 코드의 재사용성이 뛰어나며, 변경사항은 부모 클래스에만 반영해도 자식 클래스에 반영되기 때문에 유지보수성 면에서도 좋다.</p>
<blockquote>
<p>클래스의 생성자(Constructor)는 클래스의 멤버에 해당하지 않는다. 그래서 자식 클래스는 부모 클래스의 생성자를 상속하지는 않지만, <code>super()</code> 키워드를 통해 호출할 수는 있다.</p>
</blockquote>
<blockquote>
<p>부모 클래스와 자식 클래스가 같은 패키지 안에 위치하면 자식 클래스는 부모 클래스의 <code>default</code> (패키지 범위 제한) 멤버 또한 상속한다. </p>
</blockquote>
<blockquote>
<p>부모 클래스의 <code>private</code> 필드 및 메서드는 자식 클래스가 상속할 수 없지만, 부모 클래스의 중첩 클래스는 <code>private</code> 필드 및 메서드에 접근할 수 있다. 이 때문에 중첩 클래스가 존재하는 부모 클래스를 상속하는 자식 클래스는 부모 클래스의 <code>private</code> 멤버에 간접적으로 접근할 수 있다. </p>
</blockquote>
<p>클래스는 <code>extends</code> 키워드를 사용해 상속한다. 각 클래스는 하나의 클래스만 상속할 수 있는데, 다중상속을 허용하면 계층간 구조가 난잡해지기 때문이다. </p>
<p>하지만 자식 클래스가 다른 클래스의 부모 클래스가 될 수는 있다. 즉, 상속하는 클래스를 상속하는 클래스가 존재할 수 있다. 이 상속의 계층 구조의 가장 위에는 <code>Object</code> 클래스가 존재한다.</p>
<h3 id="object-클래스">Object 클래스</h3>
<p><code>Object</code> 클래스는 모든 클래스의 조상격인 클래스다. <code>java.lang</code> 패키지에 정의되어 있으며, 모든 클래스에 공통되는 것을 정의한다. </p>
<h2 id="그럼-상속의-장점은-무엇인가">그럼 상속의 장점은 무엇인가?</h2>
<p>자식 클래스는 상속한 부모 클래스의 멤버를 (1) 사용하거나, (2) 대체하거나, (3) 보강하거나 (4) 숨길 수 있다.</p>
<h4 id="필드">필드</h4>
<ul>
<li>부모 클래스에서 상속된 필드는 자식 클래스에서 직접적으로 사용할 수 있다</li>
<li>부모 클래스에서 상속된 필드와 같은 필드를 자식 클래스에서 선언하여 상속된 필드를 숨길 수 있다. (추천되지 않는다)</li>
<li>부모 클래스에서 존재하지 않는 필드도 자식 클래스에서 새로 정의할 수 있다.</li>
</ul>
<h4 id="메서드">메서드</h4>
<ul>
<li>부모 클래스에서 상속한 메서드를 자식 클래스에서 그대로 사용할 수 있다.</li>
<li>부모 클래스에서 상속한 메서드와 같은 시그니처<em>를 갖는 메서드를 자식 클래스에 정의하여 *</em>오버라이딩(Overriding)**할 수 있다. </li>
<li>부모 클래스에서 상속한 <code>static</code> 메서드와 같은 시그니처를 갖는 <code>static</code> 메서드를 자식 클래스에 정의하여 부모 클래스의 메서드를 숨길 수 있다.</li>
<li>부모 클래스에 존재하지 않는 메서드를 자식 클래스에 정의할 수 있다.</li>
<li><code>super</code> 키워드를 사용하여 부모 클래스의 생성자를 호출할 수 있다.</li>
</ul>
<blockquote>
<p>*메서드 시그니처 (Method Signature)는 메서드명과 메서드의 매개변수를 포함한다. 
메서드 시그니처, 그리고 (메서드 시그니처에는 포함되지 않는) 리턴 타입까지 컴파일 타임에 바인딩되어 바이트코드에 포함된다. 리턴 타입은 시그니처에는 포함되지 않지만, 오버로딩과 같은 목적으로 컴파일 타임에 결정된다.</p>
</blockquote>
<h3 id="형-변환-type-casting">형 변환 (Type Casting)</h3>
<p>상속의 또 다른 장점은 형 변환이다. </p>
<h4 id="묵시적-형-변환">묵시적 형 변환</h4>
<p>자식 클래스와 부모 클래스 간에는 <code>is-a</code> 관계가 성립된다. 예를 들어, <code>Jacket</code> 클래스가 <code>Clothes</code> 클래스를 상속한다. 그러면 <code>Jacket</code> is a <code>Clothes</code>가 성립한다. (역은 성립하지 않는다)</p>
<p>그렇기 때문에 부모 클래스 타입을 선언된 변수에 자식 클래스로 인스턴스화가 가능하다. </p>
<pre><code class="language-java">Jacket j1 = new Jacket();
Clothes c1 = new Jacket();
Object o1 = new Jacket();</code></pre>
<p><code>Object</code> 클래스는 모든 클래스의 조상 클래스이기 때문에 인스턴스화가 가능한 클래스라면 모두 <code>Object</code> 변수에 대해 인스턴스화할 수 있다. </p>
<p>위 예시처럼, 더 좁은 범위의 클래스 타입에서 더 넓은 범위의 클래스 타입으로 형 변환하는데는 <code>=</code> 연산자로 충분하다. 이를 <strong>묵시적 형 변환</strong>이라 한다.</p>
<h4 id="명시적-형-변환">명시적 형 변환</h4>
<p>하지만 역은?</p>
<pre><code class="language-java">Jacket j2 = o1;</code></pre>
<p>위 코드는 컴파일 타임 에러가 발생한다. 코드를 쓴 우리는 <code>o1</code>이 <code>Jacket()</code>으로 인스턴스화된 것을 알지만, 컴파일러는 이를 모르기 때문이다. 그래서 <code>o1</code>이 <code>Jacket</code> 타입임을 우리가 컴파일러에 명시하고, 약속해 주어야 한다. </p>
<pre><code class="language-java">Jacket j2 = (Jacket) o1;</code></pre>
<p>위 코드처럼 형 변환을 명시하면, 컴파일러는 <code>o1</code>이 <code>Jacket</code> 타입일거라 간주하고 오류를 발생시키지 않는다. 하지만, 만약 <code>o1</code>이 <code>Jacket</code> 타입이 아니라면, 런타임에 예외가 발생할 것이다. </p>
<p>실제로 명시적 형 변환을 쓸 때는 이런 예외를 미연에 방지하기 위해 <code>instanceof</code> 연산자를 활용한다</p>
<pre><code class="language-java">if (o1 instanceof Jacket) {
    Jacket j2 = (Jacket) o1;
}</code></pre>
<h4 id="형-변환의-장점">형 변환의 장점</h4>
<p>형 변환을 사용했을 때 가장 직관적인 장점은 매개변수의 활용이다.</p>
<p>메서드의 매개변수를 지정할 때는 매개변수의 타입을 지정해야 하는데, <code>Jacket</code> 타입, <code>Dress</code> 타입, <code>Pants</code> 타입마다 메서드를 생성하면 반복적이고, 효율적이지 못하다.</p>
<p>이럴 때 이 세 클래스의 부모 클래스인, <code>Clothes</code> 타입으로 매개변수를 선언하면 각각의 인스턴스 또한 매개변수로 받을 수 있기 때문에 편리하다.</p>
<hr />
<h1 id="추상화-abstraction">추상화, Abstraction</h1>
<p>객체를 사용하기 위해서 객체의 모든 로직과 속성, 행위를 파악해야 한다면 필요 이상으로 까다로울 것이다. </p>
<p>운전을 하기 위해서 차량 엔진이 어떻게 동작하는지 알 필요 없듯이, 객체를 사용하기 위해서 클래스의 내부를 전부 알 필요는 없다. </p>
<p>그래서 인터페이스(Interface) 또는 추상 클래스 (Abstract Class)를 통해 주요한 디테일을 명시하고, 상세한 디테일은 해당 인터페이스를 구현하는, 또는 해당 추상 클래스를 상속하는 클래스에 구현한다.</p>
<h3 id="추상-클래스-abstract-class">추상 클래스, Abstract Class</h3>
<p>추상 클래스는 <code>abstract</code> 키워드로 선언된 클래스로, 추상 메서드를 선언할 수 있는 클래스다. (꼭 추상 메서드를 선언할 필요는 없다.) 추상이기 때문에 인스턴스화 할 수는 없지만 상속될 수는 있다.</p>
<p>그럼 추상 메서드는 무엇인가? 간단히 말하면 구현을 하지 않고, 선언만 한 메서드다. <code>abstract</code> 키워드와 함께 리턴 타입(Return Type), 메서드명, 각 매개변수의 타입 및 변수명을 포함한다.</p>
<pre><code class="language-java">abstract void moveTo(double deltaX, double deltaY);</code></pre>
<blockquote>
<p>메서드 시그니처 (Method Signature)는 메서드명과 메서드의 매개변수를 포함한다. 
메서드 시그니처, 그리고 (메서드 시그니처에는 포함되지 않는) 리턴 타입까지 컴파일 타임에 바인딩되어 바이트코드에 포함된다. 리턴 타입은 시그니처에는 포함되지 않지만, 오버로딩과 같은 목적으로 컴파일 타임에 결정된다.</p>
</blockquote>
<p>그래서 추상 메서드를 선언하는 클래스는 꼭 추상 클래스로 선언해야 한다. </p>
<p>이 추상 클래스를 상속하는 클래스는 주로 부모 클래스의 추상 메서드를 구현하는 역할을 수행한다. <code>extends</code> 키워드를 활용해 클래스의 상속을 명시한다. 
추상 클래스를 상속하는 서브클래스가 그 클래스의 추상 메서드를 구현하지 않는다면 서브클래스 또한 <code>abstract</code>로 선언되어야 한다. </p>
<h3 id="인터페이스-interface">인터페이스, Interface</h3>
<p>인터페이스는 추상 클래스 중 오직 추상 메서드만 갖는 클래스와 같다 볼 수 있다.</p>
<pre><code class="language-java">interface Animal {
    public void animalSound(String animalType);
    public void run();
}</code></pre>
<p>추상 클래스의 추상 메서드와 같이 리턴 타입, 메서드명, 그리고 매개변수의 타입 및 변수명을 선언한다.
다른 점은 <code>abstract</code>로 선언할 필요가 없다는 점이다. 이미 인터페이스로 선언한 것만으로 여기에서 선언될 모든 메서드가 추상 메서드임을 인지하기 때문에 <code>abstract</code>로 추상 메서드와 구현 메서드를 구분할 필요가 없다. </p>
<p>인터페이스를 구현하는 클래스는 <code>implements</code> 키워드로 구현 관계를 명시한다. 이제 해당 클래스는 인터페이스에서 선언된 모든 메서드들을 구현하도록 컴파일러가 강제한다. 구현하지 않을 경우, 컴파일 에러가 발생한다. </p>
<p>이런 점에 있어서 인터페이스는 메서드에 대한 '약속'으로 이해할 수 있다. 인터페이스를 구현하는 클래스는 이 인터페이스의 메서드의 리턴 타입, 메서드명, 그리고 매개변수에다가 로직을 더해 구현하겠다고 약속하는 것과도 같다. </p>
<h3 id="인터페이스와-추상-클래스의-차이">인터페이스와 추상 클래스의 차이</h3>
<p>인터페이스와 추상 클래스 모두 인스턴스화가 되지 않는다는 점, 그리고 주된 목적이 추상화라는 점에서 공통점이 존재한다. </p>
<p>하지만 다음과 같은 차이도 존재한다.</p>
<ol>
<li>변수 선언에 대한 제한</li>
</ol>
<p>인터페이스의 모든 필드는 <code>public</code>, <code>static</code>, <code>final</code>(3가지 모두) 이어야 한다. 하지만 추상 클래스에는 <code>static</code>이나 <code>final</code>하지 않은 필드를 선언할 수 있다.</p>
<ol start="2">
<li>메서드 선언에 대한 제한</li>
</ol>
<p>Java7까지는 인터페이스가 구현 메서드를 가질 수 없었다. 그래서 추상 클래스는 추상 메서드와 구현 메서드 모두 가질 수 있다는 점에서 차이가 확연했다.</p>
<h4 id="하지만-java8에-default-키워드가-추가되었다">하지만 <strong>Java8에 <code>default</code> 키워드가 추가되었다</strong>.</h4>
<p>이 때부터 인터페이스의 메서드는 추상 관련 키워드를 사용하지 않거나, <code>abstract</code> 또는 <code>default</code> 키워드를 사용할 수 있다.</p>
<p><code>abstract</code>를 명시하거나, 추상 관련 키워드를 사용하지 않은 메서드는 각각 명시적, 묵시적으로 추상 메서드를 선언한다. 그래서 해당 메서드는 바디를 가질 수 없다.</p>
<p>하지만 <code>default</code> 키워드를 명시하는 메서드는 바디를 가질 수 있게 되어 추상 클래스의 이점이였던 구현 메서드와 대등해졌다.</p>
<p>여전히 차이는 존재한다. </p>
<p>추상 클래스는 <code>public</code> 또는 <code>protected</code>로 추상 메서드를 선언할 수 있고, 구현 메서드는 <code>private</code>으로도 선언할 수 있다.</p>
<p>반면에 인터페이스의 메서드는 무조건 <code>public</code>으로 선언되고, 인터페이스를 구현하는 클래스가 인터페이스의 메서드를 구현할 때는 해당 메서드의 범위(scope) 이상이어야 하기 때문에 마찬가지로 <code>public</code>이어야만 한다.</p>
<p>또한, 클래스는 하나의 추상 클래스만을 상속할 수 있지만, 여러 인터페이스를 구현할 수 있기 때문에 추상 클래스를 써야 할 이유가 적어졌다.</p>
<h3 id="추상-클래스가-인터페이스를-구현하면">추상 클래스가 인터페이스를 구현하면?</h3>
<p>인터페이스를 구현(implement)하는 클래스는 인터페이스에 선언된 모든 메서드를 구현해야 한다.</p>
<p>하지만, 추상 클래스가 인터페이스를 구현한다면 인터페이스의 모든 메서드를 구현할 필요가 없다.</p>
<p>만약 이 추상 클래스를 상속하는 구현 클래스가 있다면 이 구현 클래스는 추상 클래스가 구현하지 않은 메서드까지 모두 구현해야 한다.</p>
<hr />
<h1 id="다형성-polymorphism">다형성, Polymorphism</h1>
<p>마지막으로, 다형성이다. 다형성의 사전적 의미는 생물학에서 생물이 다양한 형태 또는 성질을 의미한다. Java에서도 말 그대로 하나의 사물이 다양한 형태를 갖는다는 뜻이다.</p>
<p>실생화에는, 예를 들어, 남자가 존재한다. 이 남자는 가정에서는 아버지이자 남편이고, 회사에서는 팀장이다. 각기 상황에 따라 다른 '형태'를 띄는 것이다. </p>
<h3 id="동적-바인딩-런타임-다형성">동적 바인딩, 런타임 다형성</h3>
<p>클래스 또한 다양한 '형태'를 가질 수 있는데, 이에 대표적인 예시가 인터페이스와 상속이다.</p>
<p>인터페이스, 추상클래스, 그리고 상속에서 알아봤듯이, 클래스를 인스턴스화할 때 꼭 자신의 형으로 선언할 필요는 없다. 자신이 상속하는 부모 클래스, 구현하는 추상 클래스 또는 인터페이스의 형으로 선언할 수 있다.</p>
<p>이 중 상속, 특히 오버라이딩에서 다형성을 확인할 수 있다.</p>
<p><code>Bicycle</code> 클래스를 상속하는 <code>MountainBike</code> 클래스와 <code>RoadBike</code> 클래스가 있다. <code>MountainBike</code> 클래스와 <code>RoadBike</code> 각각에서 <code>Bicycle</code> 클래스에 정의된 메서드 <code>printDescription()</code>를 오버라이딩하는 메서드를 정의한다. </p>
<p><code>MountainBike</code> 클래스와 <code>RoadBike</code> 클래스는 <code>Bicycle</code> 클래스를 상속하기 때문에 <code>Bicycle</code> 형의 변수에 인스턴스화할 수 있다.</p>
<pre><code class="language-java">public class TestBikes {
  public static void main(String[] args){
    Bicycle bike01, bike02, bike03;

    bike01 = new Bicycle(20, 10, 1);
    bike02 = new MountainBike(20, 10, 5, &quot;Dual&quot;);
    bike03 = new RoadBike(40, 20, 8, 23);

    bike01.printDescription();
    bike02.printDescription();
    bike03.printDescription();
  }
}</code></pre>
<p>위 코드에서 <code>bike01</code>, <code>bike02</code>, <code>bike03</code>는 각각 인스턴스화한 클래스의 <code>printDescription()</code>을 사용한다.</p>
<p>이렇게 같은 타입의 변수더라도 구현체에 따라 다른 형태를 가질 수 있는 것이 다형성 중 동적 바인딩에 해당한다. </p>
<p>오버라이딩은 런타임에 해결되기 때문에 동적 바인딩이라 불린다. 다음으로 설명할 컴파일 타임에 진행되는 정적 바인딩에 비해 메모리 및 시간 효율성 면에서 아쉽지만, 객체지향성을 잘 표현한다. </p>
<h3 id="정적-바인딩-컴파일-타임-다형성">정적 바인딩, 컴파일 타임 다형성</h3>
<p>메서드 오버로딩이 정적 바인딩에 해당한다. </p>
<p>같은 메서드명을 갖는 메서드들이 다른 매개변수들을 가지는 것을 오버로딩이라 한다. 매개변수들의 타입과 개수로 구분할 수 있다. </p>
<hr />
<p>객체지향의 4가지 핵심 개념을 이해하고, 활용해서 프로그래밍하는 것이 Java를 잘 활용하는 코딩 아닐까?</p>
<hr />
<p>출처:</p>
<ul>
<li><a href="https://docs.oracle.com/javase/tutorial/java/concepts/interface.html">https://docs.oracle.com/javase/tutorial/java/concepts/interface.html</a></li>
<li><a href="https://docs.oracle.com/javase/tutorial/java/IandI/abstract.html">https://docs.oracle.com/javase/tutorial/java/IandI/abstract.html</a></li>
<li><a href="https://docs.oracle.com/javase/tutorial/java/javaOO/methods.html">https://docs.oracle.com/javase/tutorial/java/javaOO/methods.html</a></li>
<li><a href="https://stackoverflow.com/questions/9223938/java-is-method-name-signature-resolution-done-statically-compile-time">https://stackoverflow.com/questions/9223938/java-is-method-name-signature-resolution-done-statically-compile-time</a></li>
<li><a href="https://www.w3schools.com/java/java_interface.asp">https://www.w3schools.com/java/java_interface.asp</a></li>
<li><a href="https://docs.oracle.com/javase/tutorial/java/IandI/subclasses.html">https://docs.oracle.com/javase/tutorial/java/IandI/subclasses.html</a></li>
<li><a href="https://docs.oracle.com/javase/tutorial/java/javaOO/accesscontrol.html">https://docs.oracle.com/javase/tutorial/java/javaOO/accesscontrol.html</a></li>
<li><a href="https://docs.oracle.com/en/database/oracle/oracle-database/12.2/jjdev/Java-overview.html">https://docs.oracle.com/en/database/oracle/oracle-database/12.2/jjdev/Java-overview.html</a></li>
<li><a href="https://ioflood.com/blog/encapsulation-java/">https://ioflood.com/blog/encapsulation-java/</a></li>
<li><a href="https://www.geeksforgeeks.org/polymorphism-in-java/?_gl=1*2a0sbw*_ga*LXJzWWU1ek0yaUZpdjlRbENuTG9uZkZhQnBHU0stUnhkXzd3MUpyanRMRmQ0aktYdUdRemdZSTU0dDRONU1sMA..*_ga_E752F18V9F*MTcyMTE0MTM4Ny43LjEuMTcyMTE0MTQzMi4wLjAuMA">https://www.geeksforgeeks.org/polymorphism-in-java/?_gl=1*2a0sbw*_ga*LXJzWWU1ek0yaUZpdjlRbENuTG9uZkZhQnBHU0stUnhkXzd3MUpyanRMRmQ0aktYdUdRemdZSTU0dDRONU1sMA..*_ga_E752F18V9F*MTcyMTE0MTM4Ny43LjEuMTcyMTE0MTQzMi4wLjAuMA</a>..</li>
<li><a href="https://docs.oracle.com/javase/tutorial/java/javaOO/accesscontrol.html">https://docs.oracle.com/javase/tutorial/java/javaOO/accesscontrol.html</a></li>
<li><a href="https://docs.oracle.com/javase/tutorial/java/IandI/polymorphism.html">https://docs.oracle.com/javase/tutorial/java/IandI/polymorphism.html</a></li>
</ul>