---
title: "[JAVA] ArrayDeque를 사용해보자"
date: Thu, 01 Aug 2024 10:45:13 GMT
---

<h1 id="arraydeque">ArrayDeque</h1>
<p>ArrayDeque, 즉 Array Double Ended Queue 에 대해 알아보자. 일반적으로 Last-In, First-Out을 구현하여 배열의 끝에서 데이터를 추가하는 큐와 다르게, ArrayDeque는 큐의 양 끝에 데이터를 용이하게 추가하고 제거할 수 있다. </p>
<p>Java에서 Deque 인터페이스는 크기를 조절할 수 있는 배열에 요소를 저장하는데, ArrayDeque이 이 Deque 인터페이스를 구현한다. 크기에 제한도 없고, 배열의 양 끝에 데이터를 추가하고 제거하는 연산을 O(1) 시간복잡도에 제공하니 유용한 자료구조다. </p>
<blockquote>
<p>시간복잡도</p>
</blockquote>
<ul>
<li>자료구조 양 끝에 데이터 추가: O(1)</li>
<li>자료구조 양 끝에 데이터 삭제: O(1)</li>
</ul>
<h2 id="arraydeque의-장점">ArrayDeque의 장점</h2>
<ol>
<li>자료구조 양 끝에 데이터 추가/삭제 연산의 시간 복잡도가 O(1)이다</li>
<li>자료구조의 크기에 제한이 없다. 
데이터의 추가와 삭제에 따라 조절된다</li>
<li>메모리 면에서도 효율적이다.
링크드리스트 등과 다르게 메모리 오버헤드가 발생하지 않는다</li>
<li>thread-safe하다. 
ArrayDeque 클래스 자체는 스레드 safe하지 않지만, Collections.synchronizedDeque으로 thread-safe하게 사용할 수 있다. </li>
</ol>
<h2 id="arraydeque의-단점">ArrayDeque의 단점</h2>
<ol>
<li><p>크기가 자유롭게 조절되기는 하지만, 결국 제한이 존재하기는 한다. 이 제한을 넘으면 새로운 ArrayDeque를 만들어 사용해야 할 수 있다. </p>
</li>
<li><p>자료구조의 양 끝에서의 연산을 제하면 O(N)으로 수행되는 메서드가 많다: <code>remove</code>, <code>removeFirstOccurrence</code>, <code>removeLastOccurrence</code>, <code>contains</code>, <code>iterator.move()</code> 등</p>
</li>
</ol>
<h1 id="arraydeque의-특징">ArrayDeque의 특징</h1>
<ul>
<li>null 값을 허용하지 않는다</li>
<li>스택을 구현할 때 Stack 클래스를 사용하는 것보다 빠를 가능성이 높다</li>
<li>큐를 구현할 때 LinkedList보다 빠를 가능성이 높다</li>
</ul>
<h1 id="arraydeque의-메서드">ArrayDeque의 메서드</h1>
<h4 id="1-생성자">1. 생성자</h4>
<p>기본 생성자: 16개 원소를 저장할 수 있는 빈 array deque을 생성함</p>
<pre><code class="language-java">ArrayDeque&lt;Integer&gt; arrayDeque = new ArrayDeque&lt;&gt;();</code></pre>
<p>Collection으로 ArrayDeque 생성하기</p>
<pre><code class="language-java">ArrayDeque&lt;Integer&gt; arrayDeque = new ArrayDeque&lt;&gt;(arrList);</code></pre>
<p>ArrayDeque의 요소 개수를 정의하여 생성하기</p>
<pre><code class="language-java">ArrayDeque&lt;Integer&gt; arrayDeque = new ArrayDeque&lt;&gt;(int numElements);</code></pre>
<h4 id="2-데이터-추가">2. 데이터 추가</h4>
<p>덱의 끝에 데이터 추가</p>
<pre><code class="language-java">boolean added = arrayDeque.add(5);

// void
arrayDeque.addLast(5);
arrayDeque.push(5);</code></pre>
<p>덱의 맨 앞에 데이터 추가</p>
<pre><code class="language-java">// void
arrayDeque.addFirst(5);</code></pre>
<h4 id="3-데이터-포함-여부-확인">3. 데이터 포함 여부 확인</h4>
<pre><code class="language-java">boolean contains = arrayDeque.contains(5);</code></pre>
<h4 id="4-데이터-조회">4. 데이터 조회</h4>
<pre><code class="language-java">int first = arrayDeque.getFirst();
int last = arrayDeque.getLast();</code></pre>
<h4 id="5-데이터-삭제">5. 데이터 삭제</h4>
<p>덱의 첫 요소를 제거해서 리턴</p>
<pre><code class="language-java">arrayDeque.poll(); // 비었을 경우 null 반환
arrayDeque.pollFirst(); // 비었을 경우 null 반환
arrayDeque.removeFirst();</code></pre>
<p>덱의 마지막 요소 제거해서 리턴</p>
<pre><code class="language-java">arrayDeque.pollLast(); // 비었을 경우 null 반환
arrayDeque.pop();
arrayDeque.removeLast();</code></pre>
<p>덱의 특정 요소를 찾아서 제거 (첫 요소부터 순차적으로 탐색)</p>
<pre><code class="language-java">// boolean 리턴
arrayDeque.removeFirstOccurrence(5);
arrayDeque.removeLastOccurrence(5);</code></pre>
<hr />
<p>출처: 
<a href="https://docs.oracle.com/javase/8/docs/api/java/util/ArrayDeque.html">https://docs.oracle.com/javase/8/docs/api/java/util/ArrayDeque.html</a>
<a href="https://www.geeksforgeeks.org/arraydeque-in-java/">https://www.geeksforgeeks.org/arraydeque-in-java/</a></p>