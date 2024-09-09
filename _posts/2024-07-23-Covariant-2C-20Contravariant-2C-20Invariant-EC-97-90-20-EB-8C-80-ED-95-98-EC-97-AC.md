---
title: "Covariant, Contravariant, Invariant에 대하여"
date: 2024-07-23T00:47:10+00:00
---

<p>형 변환에 대해 파고들면 <strong>Covariant</strong>, <strong>Contravariant</strong>, <strong>Invariant</strong>과 같은 용어들을 쉽게 만날 수 있다. </p>
<p>세 용어 모두 형 변환에 있어 슈퍼타입-서브타입 관계성을 정의한다. </p>
<p><code>A</code>와 <code>B</code>를 타입, <code>f</code>를 형 변환, 그리고 <code>&lt;=</code>을 서브타입 관계성이라 가정하자. (즉, <code>A&lt;=B</code>는 <code>A</code>가 <code>B</code>의 서브타입을 의미한다)</p>
<ul>
<li><code>A&lt;=B</code>일 때 <code>f(A) &lt;= f(B)</code>면 <strong>Covariant</strong></li>
<li><code>A&lt;=B</code>일 때 <code>f(B) &lt;= f(A)</code>면 <strong>Contravariant</strong></li>
<li>위 두가지 상황에 모두 해당하지 않으면 <strong>Invariant</strong></li>
</ul>
<p><code>f(A) = List&lt;A&gt;</code>로 다시 확인해보자</p>
<ul>
<li><strong>Covariant</strong>면 <code>List&lt;String&gt;</code>이 <code>List&lt;Object&gt;</code>의 서브타입임을 의미한다.</li>
<li><strong>Contravariant</strong>면 <code>List&lt;Object&gt;</code>이 <code>List&lt;String&gt;</code>의 서브타입임을 의미한다.</li>
<li><strong>Invariant</strong>면 <code>List&lt;String&gt;</code>와 <code>List&lt;Object&gt;</code>는 서로 변환되지 않는, <code>String</code>과 <code>Object</code>간 서브 타입 관계성이 사라짐을 의미한다. </li>
</ul>
<h3 id="covariant">Covariant</h3>
<p>Java에서<code>f(A) = A[]</code>는 <strong>Covariant</strong>하다. 즉, <code>String[]</code>은 <code>Object[]</code>의 서브타입에 해당한다. </p>
<h3 id="invariant와-wildcard">Invariant와 Wildcard</h3>
<p>Java에서는 <code>List&lt;String&gt;</code>과 <code>List&lt;Object&gt;</code>는 <strong>Invariant</strong>하다. Generics 자체가 invariant로 인정되는 경우가 많다. </p>
<p>또 예를 들자면, <code>Integer</code>는 <code>Number</code>의 서브 타입이지만, <code>List&lt;Integer&gt;</code>는 <code>List&lt;Number&gt;</code>의 서브 타입이 아니다. 이 둘의 공통 부모는 <code>List&lt;?&gt;</code> 뿐이다. </p>
<p><img alt="" src="https://velog.velcdn.com/images/becooq81/post/aeb15743-299f-4f5f-98d5-2d6f3bcc4003/image.png" />
출처: 오라클 공식 문서</p>
<p>그래서 <strong>Invariant</strong> 관계에 놓인 이 두 리스트에 대해 관계성을 형성하기 위해서는 와일드카드를 사용해야 한다.</p>
<pre><code class="language-java">List&lt;? extends Integer&gt; intList = new ArrayList&lt;&gt;();
List&lt;? extends Number&gt;  numList = intList;  </code></pre>
<p><code>List&lt;? extends Number&gt; numList</code>는 <code>Number</code>의 서브타입 (<code>Integer</code>도 해당)의 리스트를 모두 허용하기 때문에 <code>numList</code>에 <code>intList</code>를 지정할 수 있다. </p>
<hr />
<p><a href="https://stackoverflow.com/questions/8481301/covariance-invariance-and-contravariance-explained-in-plain-english">https://stackoverflow.com/questions/8481301/covariance-invariance-and-contravariance-explained-in-plain-english</a>
<a href="https://docs.oracle.com/javase/tutorial/java/generics/subtyping.html">https://docs.oracle.com/javase/tutorial/java/generics/subtyping.html</a></p>