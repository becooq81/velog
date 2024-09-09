---
title: "[JAVA] long보다 큰 숫자 BigInteger"
date: Tue, 06 Aug 2024 03:46:38 GMT
---

<p>알고리즘을 풀면서 long보다 큰 범위를 필요로 하는 문제는 처음 만났다.  <a href="https://www.acmicpc.net/problem/1914">백준 #1914</a></p>
<p>long보다 큰 범위의 정수를 사용하기 위해서 <code>BigInteger</code> 클래스가 존재한다.</p>
<h1 id="biginteger">BigInteger</h1>
<p><code>java.math</code>에서 가져와서 사용할 수 있다.</p>
<pre><code class="language-java">import java.math.BigInteger;</code></pre>
<h2 id="초기화">초기화</h2>
<h4 id="1-정수로-초기화">1. 정수로 초기화</h4>
<pre><code class="language-java">BigInteger A = BigInteger.valueOf(54);</code></pre>
<h4 id="2-string으로-초기화">2. String으로 초기화</h4>
<p>long보다 큰 범위의 값으로 초기화해야 할 때 유용할 것이다</p>
<pre><code class="language-java">BigInteger A = BigInteger.valueOf(&quot;123958123123&quot;);</code></pre>
<h4 id="3-biginteger에서-정의된-숫자-값">3. BigInteger에서 정의된 숫자 값</h4>
<pre><code class="language-java">BigInteger A = BigInteger.ONE;
A = BigInteger.ZERO;
A = = BigInteger.TEN;</code></pre>
<h2 id="연산">연산</h2>
<h4 id="1-덧셈">1. 덧셈</h4>
<p><code>BigInteger bigInteger1.add(bigInteger2)</code></p>
<pre><code class="language-java">A.add(new BigInteger(&quot;1235321&quot;));</code></pre>
<h4 id="2-뺄셈">2. 뺄셈</h4>
<p><code>BigInteger bigInteger.subtract(bigInteger2)</code></p>
<h4 id="3-나눗셈">3. 나눗셈</h4>
<p><code>BigInteger bigInteger1.divide(bigInteger2)</code></p>
<h4 id="4-곱셈">4. 곱셈</h4>
<p><code>BigInteger bigInteger1.multiply(bigInteger2)</code></p>
<h4 id="5-제곱">5. 제곱</h4>
<p><code>BigInteger bigInteger1.multiply(int1)</code></p>
<p>지수는 int 값이지만 리턴 값은 BigInteger다.</p>
<h4 id="6-제곱근">6. 제곱근</h4>
<p><code>BigInteger bigInteger1.sqrt()</code></p>
<hr />
<p><a href="https://www.geeksforgeeks.org/biginteger-class-in-java/">https://www.geeksforgeeks.org/biginteger-class-in-java/</a></p>