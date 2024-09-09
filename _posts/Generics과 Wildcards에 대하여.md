<blockquote>
<p>Oracle의 공식 문서를 참고하여 작성한 포스트입니다</p>
</blockquote>
<h1 id="generics란">Generics란?</h1>
<p>JDK 5.0부터 생긴 Generics는 특히 <code>Java.util.Collections</code>에서 더 안전한, 컴파일 단에서 보증하는 코드를 짜는데 혁신적이다.</p>
<p>예시로 확인해보자</p>
<p>다음 코드는 Generics를 사용하지 않고 컬렉션의 요소 중 길이가 4인 String을 제거하는 코드다.</p>
<pre><code class="language-java">// Removes 4-letter words from c. Elements must be strings
static void expurgate(Collection c) {
    for (Iterator i = c.iterator(); i.hasNext(); )
      if (((String) i.next()).length() == 4)
        i.remove();
}</code></pre>
<p>개발자는 인자로 들어올 컬렉션이 당연히 String 타입일 거라 확신하고 if 조건에 형 변환을 수행하는 코드를 짰지만, 과연 확실한가?</p>
<p>요소가 무조건 String 타입일 것이라는 보장이 있나?</p>
<p>없다. 하지만 String 타입이 아닌 요소가 있더라도 컴파일 타임에는 확인할 수가 없고, 런타임에 에러가 발생할 것이다.</p>
<p>이런 리스크를 해결해주는 것이 바로 Generic이다.</p>
<pre><code class="language-java">// Removes the 4-letter words from c
static void expurgate(Collection&lt;String&gt; c) {
    for (Iterator&lt;String&gt; i = c.iterator(); i.hasNext(); )
      if (i.next().length() == 4)
        i.remove();
}</code></pre>
<p>인자에 꺽새와 그 꺽새에 담긴 String이 추가되었다. 이제 <code>Collection&lt;String&gt; c</code>로 바뀐 인자는 꼭 String 타입을 원소로 갖는 컬렉션만 인자로 받을 것을 컴파일 단계에서 명시한다. </p>
<p>Iterator에도 Generic Type을 명시하여 형 변환을 더 이상 필요로 하지 않는다. </p>
<p>이렇게 Generics는 우리에게 더 안전하고, 간소화된 코드를 짤 수 있게 해주는 도구다. </p>
<h3 id="형-인자">형 인자</h3>
<pre><code class="language-java">public interface List &lt;E&gt; {
    void add(E x);
    Iterator&lt;E&gt; iterator();
}

public interface Iterator&lt;E&gt; {
    E next();
    boolean hasNext();
}</code></pre>
<p>위 코드와 같이 <code>E</code>와 같은 Generic Type을 꺽새에 담아 표현할 수 있다.</p>
<p><code>Collections</code>의 <code>List</code>에 담기는 건 원소(Element)니까 <code>E</code>, <code>HashMap</code>과 같이 키-값 짝으로 담기는 경우에는 <code>K</code> (Key), <code>V</code> (Value), <code>T</code>는 Type, <code>N</code>은 Number 등 어떤 값을 추상화하는 지에 따라 다른 알파벳을 사용한다. </p>
<h3 id="erasure-형">Erasure 형</h3>
<p>Generics는 <code>erasure</code> type으로 구현된다. <code>Erasure</code> 형은 컴파일 타임에만 사용되고, 컴파일러에 의해 지워지는 타입을 의미한다. </p>
<p>타입 erasure 과정에서 컴파일러는 모든 타입 파라미터를 제거하고 제한이 있는 타입 (bounded)이면 첫 제한의 타입으로 대체하고, 제한이 없으면 <code>Object</code> 타입으로 대체한다. </p>
<p>제네릭 메서드에 있어서도 제네릭 타입을 첫 제한의 타입으로 대체한다.</p>
<pre><code class="language-java">public static &lt;T extends Shape&gt; void draw(T shape) { /* ... */ }</code></pre>
<p>위와 같은 코드는 아래와 같이 컴파일된다.</p>
<pre><code class="language-java">public static void draw(Shape shape) { /* ... */ }</code></pre>
<p>그럼<code>erasure</code> 형을 왜 쓸까? 제네릭과는 반대로 인자로 타입을 명시하지 않는 레거시 코드 (legacy code)와 제네릭 코드 간 호환을 가능하게 해주는 것이 바로 Generics의 <code>erasure</code> 특성이다.</p>
<p>하지만 이 특성에 단점도 존재한다. 인자의 타입 정보가 런타임에는 사라지기 때문에 제네릭에 의해 자동으로 생성된 캐스팅이 레거시 코드와 호환되지 않을 수 있다. </p>
<p>이 단점에 대한 해결 방안은 <code>java.util.Collections</code>에서 제공하는 <strong>checked collection wrappers</strong>를 사용하는 것이다. </p>
<p>Checked collection wrappers는 런타임에 타입 안정성을 보장해서 타입에 맞지 않은 코드에 대해 에러를 발생시킨다. </p>
<pre><code class="language-java">Set&lt;String&gt; s = new HashSet&lt;String&gt;();</code></pre>
<p>위와 같이 <code>HashSet</code>을 사용하는 게 일반적인 방법이라면, checked collection wrappers는 아래와 같이 사용할 수 있다.</p>
<pre><code class="language-java">Set&lt;String&gt; s = Collections.checkedSet(new HashSet&lt;String&gt;(), String.class);</code></pre>
<p>이 방식으로 <code>Set</code>을 초기화할 경우, 런타임에 레거시 코드가 <code>Integer</code>와 같은 타입의 값을 추가하고자 했을 때 <code>ClassCastException</code>을 발생시킨다. </p>
<h2 id="generic-methods">Generic Methods</h2>
<p><strong>Generic Method</strong>는 자신의 타입 파라미터를 정의하는 메서드다. 제네릭 타입을 정의하는 것과 유사하지만, 타입 파라미터의 범위가 자신이 정의된 메서드 내부로 제한된다는 점에서 차이가 있다. 또한, static, non-static 제네릭 메서드를 정의할 수 있고, 제네릭한 클래스 생성자도 가능하다. </p>
<p>제네릭 메서드의 특징은 꺽새 안에 들어가는 타입 파라미터 집합이다. 특히 static 제네릭 메서드의 타입 파라미터들은 메서드의 리턴 타입 전에 존재해야 한다.</p>
<pre><code class="language-java">public class Util {
    public static &lt;K, V&gt; boolean compare(Pair&lt;K, V&gt; p1, Pair&lt;K, V&gt; p2) {
        return p1.getKey().equals(p2.getKey()) &amp;&amp; p1.getValue().equals(p2.getValue());
    }
}

public class Pair&lt;K, V&gt; {

    private K key;
    private V value;

    public Pair(K key, V value) {
        this.key = key;
        this.value = value;
    }

    public void setKey(K key) { this.key = key; }
    public void setValue(V value) { this.value = value; }
    public K getKey()   { return key; }
    public V getValue() { return value; }
}</code></pre>
<p>위와 같이 제네릭 타입을 정의하고, 이를 활용하는 제네릭 메서드를 정의할 수 있다.</p>
<pre><code class="language-java">Pair&lt;Integer, String&gt; p1 = new Pair&lt;&gt;(1, &quot;apple&quot;);
Pair&lt;Integer, String&gt; p2 = new Pair&lt;&gt;(2, &quot;pear&quot;);
boolean same = Util.&lt;Integer, String&gt;compare(p1, p2);</code></pre>
<p>위 코드에서는 <strong>Type Witness</strong>로 메서드의 제네릭 타입을 상세 타입으로 명시할 수 있다. </p>
<p>아래와 같이, Type Witness를 명시하지 않고, 컴파일러가 타입을 맞추는 타입 추론 (Type Inference)를 활용할 수도 있다.</p>
<pre><code class="language-java">Pair&lt;Integer, String&gt; p1 = new Pair&lt;&gt;(1, &quot;apple&quot;);
Pair&lt;Integer, String&gt; p2 = new Pair&lt;&gt;(2, &quot;pear&quot;);
boolean same = Util.compare(p1, p2);</code></pre>
<h1 id="type-inference">Type Inference</h1>
<p>그래서 타입 추론이 무엇일까?</p>
<p>Java의 컴파일러는 각 메서드의 호출 및 선언을 확인해서 그 호출을 가능케하는 타입 인수(arguments)를 결정할 수 있다. 이 추론의 과정으로 인수의 타입과 (가능하다면) 리턴 타입 등을 알아내고는 한다. </p>
<p>또한, 항상 조건을 모두 만족하는 것 중 가장 세부적인 (specific) 타입을 지정하고자 한다. </p>
<pre><code class="language-java">BoxDemo.&lt;Integer&gt;addBox(Integer.valueOf(10), listOfIntegerBoxes);
BoxDemo.addBox(Integer.valueOf(20), listOfIntegerBoxes);</code></pre>
<p>첫 줄의 코드는 Type Witness로 명시하지만, 두번째 줄은 Type Inference를 사용하는 모습을 확인할 수 있다.</p>
<p>두번째 줄의 경우에는 컴파일러가 인수의 타입을 확인해서 타입을 추론하는 과정을 거친다. </p>
<p>사실 타입 추론을 이미 사용해봤을 거다.</p>
<pre><code class="language-java">Map&lt;String, List&lt;String&gt;&gt; myMap = new HashMap&lt;String, List&lt;String&gt;&gt;();
Map&lt;String, List&lt;String&gt;&gt; myMap = new HashMap&lt;&gt;();</code></pre>
<p>두번째 라인처럼 코드를 짜면 타입 추론을 활용한 것이다.</p>
<h3 id="target-types">Target Types</h3>
<p>컴파일러가 타입을 추론할 때 타겟 타이핑(Target Typing)을 활용한다. </p>
<p><code>Collections.emptyList</code> 메서드를 확인해보자</p>
<pre><code class="language-java">static &lt;T&gt; List&lt;T&gt; emptyList();</code></pre>
<p>이 메서드의 리턴 값을 <code>List&lt;String&gt;</code>에 저장하면?</p>
<pre><code class="language-java">List&lt;String&gt; listOne = Collections.emptyList();</code></pre>
<p>여기서 <code>List&lt;String&gt;</code>이 타겟 타입이다. <code>emptyList()</code> 메서드는 <code>List&lt;T&gt;</code>를 반환하니까 이 반환 값이 저장되는 <code>List&lt;String&gt;</code> 타입일거라 간주한다</p>
<h1 id="wildcards-">Wildcards ?</h1>
<p>Generics로 웬만한 코드는 다 호환되고 컴파일 타임 안정성도 가질 것 같은데, 왜 와일드카드라는게 필요할까?</p>
<p>예시로 확인해보자 </p>
<pre><code class="language-java">void printCollection(Collection c) {
    Iterator i = c.iterator();
    for (k = 0; k &lt; c.size(); k++) {
        System.out.println(i.next());
    }
}</code></pre>
<p>위 코드에 Generics를 적용하면 아래와 같이 표현할 수 있다.</p>
<pre><code class="language-java">void printCollection(Collection&lt;Object&gt; c) {
    for (Object e : c) {
        System.out.println(e);
    }
}</code></pre>
<p>하지만 두번째 코드가 더 효율적이지 못하다.</p>
<p>첫번째 코드는 모든 컬렉션을 인자로 받을 수 있는 반면에, 두번째 코드는<code>Collection&lt;Object&gt;</code>만 받을 수 있고, 모든 컬렉션의 부모격이 아니다. </p>
<p>아래 코드는 에러를 발생시킨다.</p>
<pre><code class="language-java">Collection&lt;Object&gt; c = new ArrayList&lt;String&gt;();
ArrayList&lt;Object&gt; c = new ArrayList&lt;String&gt;();</code></pre>
<ul>
<li><code>error: incompatible types: ArrayList&lt;String&gt; cannot be converted to Collection&lt;Object&gt;</code></li>
<li><code>error: incompatible types: ArrayList&lt;String&gt; cannot be converted to ArrayList&lt;Object&gt;</code></li>
</ul>
<p>코드가 왜 에러를 발생시키는 지에 대해서는 [Covariant, Contravariant, Invariant에 대하여] (<a href="https://velog.io/@becooq81/Covariant-Contravariant-Invariant%EC%97%90-%EB%8C%80%ED%95%98%EC%97%AC">https://velog.io/@becooq81/Covariant-Contravariant-Invariant%EC%97%90-%EB%8C%80%ED%95%98%EC%97%AC</a>) 포스트에서 확인할 수 있다.</p>
<p>이러한 특성 때문에 상속 관계의 클래스들을 활용할 수 없다는 단점이 존재한다. <code>Shape</code> 클래스를 상속하는 <code>Circle</code> 클래스를 가정했을 때, <code>List&lt;Shape&gt;</code> 인자를 받는 메서드에 <code>List&lt;Circle&gt;</code>을 넘길 수 없다. 그래서 우리는 와일드카드가 필요하다. </p>
<h3 id="object과-의-차이">Object과 ?의 차이</h3>
<p>잠깐 <code>Object</code>과 ?의 차이에 대한 딴 길로 새보자</p>
<pre><code class="language-java">void printCollection(Collection&lt;?&gt; c) {
    for (Object e : c) {
        System.out.println(e);
    }
}</code></pre>
<p><code>Collection&lt;Object&gt;</code>와 <code>Collection&lt;?&gt;</code>의 차이는 무엇일까?</p>
<pre><code class="language-java">Collection&lt;Object&gt; c = new ArrayList&lt;&gt;();
c.add(5);
c.add(&quot;HELLO&quot;);
c.add(3.14);</code></pre>
<p><code>Collection&lt;Object&gt;</code>로 선언하면, <code>String</code>, <code>Integer</code>, <code>Double</code> 등등 모두 <code>Object</code> 클래스의 자식 클래스이기 때문에 어느 타입의 값이든 추가할 수 있다. 자유롭기는 하지만 코드를 짤 때 다양한 타입의 데이터를 하나의 컬렉션에 모으는 걸 의도할 일이 많지는 않을 것이다. </p>
<p><code>Collection&lt;?&gt;</code>으로 선언해보자. </p>
<pre><code class="language-java">Collection&lt;?&gt; c = new ArrayList&lt;String&gt;();
c.add(new Object()); // 컴파일 타임 에러</code></pre>
<p>흔히 위와 같이 사용할 텐데, 코드의 두번째 라인은 컴파일 타임 에러를 발생시킬 것이다. </p>
<p>와일드카드를 사용하면, 어느 인자로든 초기화가 가능하지만, 일단 초기화가 되고 나면 저장될 수 있는 형을 제한하여 stronger typing이 보장된다는 점이 장점이다. </p>
<p><code>Collection&lt;?&gt;</code>에서 값을 조회해서 저장하고 싶을 때는 <code>Object</code> 변수로 받아오면 된다. </p>
<h2 id="generic-methods-1">Generic Methods</h2>
<p>아래 코드가 왜 잘못되었는지 확인해보자</p>
<pre><code class="language-java">static void fromArrayToCollection(Object[] a, Collection&lt;?&gt; c) {
    for (Object o : a) { 
        c.add(o); // compile-time error
    }
}</code></pre>
<p>일단 <code>c</code>를 <code>Collection&lt;Object&gt;</code>로 정의했다면 <code>List&lt;String&gt;</code>, <code>HashSet&lt;Integer&gt;</code> 등등 거의 모든 종류의 인자를 받지 못한다는 것을 [WildCard] 섹션에서 확인했다. 그래서 <code>Collection&lt;?&gt;</code>로 대체했다는 것은 알겠는데, 이 코드도 컴파일 타임 에러가 난다?</p>
<p><code>Object</code> 배열의 원소인, <code>Object</code> 타입의 <code>o</code>를 와일드카드의 컬렉션에 추가하고자 하니 컴파일 타임 에러가 발생하는데, 알지 못하는 타입 (와일드카드)의 컬렉션에 무작정 <code>Object</code> 객체를 더할 수는 없기 때문이다. </p>
<p>이러한 에러에 대한 해결책이 바로 <strong>Generic Method</strong>다. Generic 타입 선언과 같이 1개 이상의 파라미터를 사용하여 Generic한 메서드를 선언할 수 있다. </p>
<pre><code class="language-java">static &lt;T&gt; void fromArrayToCollection(T[] a, Collection&lt;T&gt; c) {
    for (T o : a) {
        c.add(o); // Correct
    }
}</code></pre>
<h1 id="bounded--unbounded-wildcards">Bounded &amp; Unbounded Wildcards</h1>
<p>다시 와일드카드의 이야기로 돌아와보자</p>
<h2 id="unbounded-wildcards">Unbounded Wildcards</h2>
<p>아래 코드와 같이 물음표(?)를 사용해서 모든 타입의 인자를 가능케 하는 것이 와일드카드다. </p>
<pre><code class="language-java">public static void printList(List&lt;?&gt; list) {
    for (Object elem: list)
        System.out.print(elem + &quot; &quot;);
    System.out.println();
}</code></pre>
<p>인자의 타입에 제한을 두지 않고 와일드카드 그대로 사용하는 것을 <strong>Unbounded Wildcard</strong>라고 한다. </p>
<h2 id="upper-bounded-wildcards">Upper Bounded Wildcards</h2>
<p><code>Shape</code> 클래스를 상속하는 <code>Circle</code>, <code>Rectangle</code> 클래스를 가정했을 때, 와일드카드를 사용하면 <code>Shape</code>을 상속하는 모든 클래스의 객체를 허용하는 인자를 정의할 수 있다. </p>
<blockquote>
<p>복습! <code>List&lt;Object&gt;</code>와 <code>List&lt;String&gt;</code>은 invariant 관계성에 놓여있어 <code>Object</code>로는 위와 같은 예시가 허용되지 않는다. </p>
</blockquote>
<p>와일드카드를 사용해서 예시를 구현해보자</p>
<pre><code class="language-java">public void drawAll(List&lt;? extends Shape&gt; shapes) {
    for (Shape s : shapes) {
        s.draw(this);
    }
}</code></pre>
<p><code>List&lt;Shape&gt;</code>으로 인자를 정의했을 때는 <code>List&lt;Circle&gt;</code>와 <code>List&lt;Rectangle&gt;</code>를 인자로 받을 수 없었지만, <code>List&lt;? extends Shape&gt;</code>은 <code>Shape</code> 클래스를 상속하는 모든 클래스에 대한 <code>List</code>를 인자로 받을 수 있다. </p>
<p><code>List&lt;? extends Shape&gt;</code>를 분해해보자</p>
<ul>
<li><code>?</code> - unknown type을 의미한다. 즉, 아무거나 가능하다</li>
<li><code>extends ~</code> - '아무거나'의 제한을 정의한다. 예시에서는 <code>Shape</code>가 unknown type의 경계를 정의해서 <code>Shape</code> 클래스를 상속하는 모든 클래스를 허용한다. </li>
</ul>
<p>이렇게 <code>extends</code>를 활용해 와일드카드를 사용하는 방법을 <strong>Upper Bounded Wildcard</strong>라고 정의한다. </p>
<h3 id="와일드카드의-단점">와일드카드의 단점</h3>
<p>와일드카드의 단점이라면 제한된 범위 내의 모든 클래스를 허용하기 때문에 객체의 타입을 단언할 수 없다는 것이다. </p>
<p>아래 예시로 확인해보자</p>
<pre><code class="language-java">public void addRectangle(List&lt;? extends Shape&gt; shapes) {
    // Compile-time error!
    shapes.add(0, new Rectangle());
}</code></pre>
<p><code>Rectangle</code> 클래스가 <code>Shape</code> 클래스를 상속하기 때문에 메서드에 <code>List&lt;Rectangle&gt;</code>을 넘길 수는 있지만, 메서드 입장에서는 인자가 <code>List&lt;Rectangle&gt;</code>라 확신할 수 없다. <code>List&lt;Circle&gt;</code>이거나 <code>List&lt;Shape&gt;</code>일 수 있기 때문에 무작정 <code>shapes</code> 리스트에 <code>Rectangle</code> 객체를 추가하는 코드는 허용하지 않는다. </p>
<h2 id="lower-bounded-wildcards">Lower Bounded Wildcards</h2>
<p><code>extends</code> 키워드로 타입의 상한선을 지정하는 <strong>Upper Bounded Wildcards</strong>도 있고, <code>super</code> 키워드로 타입의 하한선을 지정하는 <strong>Lower Bounded Wildcards</strong>도 있다. </p>
<p><code>? super A</code>는 인자의 타입을 <code>A</code>와 <code>A</code>의 슈퍼 타입으로 정의한다. </p>
<p>아래 코드로 확인해보자. </p>
<pre><code class="language-java">public static void addNumbers(List&lt;? super Integer&gt; list) {
    for (int i = 1; i &lt;= 10; i++) {
        list.add(i);
    }
}</code></pre>
<p>코드에서 인자가 될 수 있는 타입은 <code>List&lt;Integer&gt;</code>와 그의 슈퍼 타입인 <code>List&lt;Number&gt;</code>, <code>List&lt;Object&gt;</code>다. </p>
<hr />
<p><a href="https://docs.oracle.com/javase/tutorial/extra/generics/intro.html">https://docs.oracle.com/javase/tutorial/extra/generics/intro.html</a>
<a href="https://docs.oracle.com/javase/tutorial/extra/generics/wildcards.html">https://docs.oracle.com/javase/tutorial/extra/generics/wildcards.html</a>
<a href="https://docs.oracle.com/javase/8/docs/technotes/guides/language/generics.html">https://docs.oracle.com/javase/8/docs/technotes/guides/language/generics.html</a>
<a href="https://docs.oracle.com/javase/tutorial/java/generics/methods.html">https://docs.oracle.com/javase/tutorial/java/generics/methods.html</a>
<a href="https://docs.oracle.com/javase/tutorial/java/generics/genTypeInference.html">https://docs.oracle.com/javase/tutorial/java/generics/genTypeInference.html</a>
<a href="https://docs.oracle.com/javase/tutorial/java/generics/capture.html">https://docs.oracle.com/javase/tutorial/java/generics/capture.html</a>
<a href="https://docs.oracle.com/javase/tutorial/java/generics/genMethods.html">https://docs.oracle.com/javase/tutorial/java/generics/genMethods.html</a></p>