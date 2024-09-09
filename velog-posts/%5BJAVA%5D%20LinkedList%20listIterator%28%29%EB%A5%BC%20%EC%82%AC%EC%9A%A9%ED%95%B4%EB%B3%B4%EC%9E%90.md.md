---
title: "[JAVA] LinkedList listIterator()를 사용해보자"
date: Tue, 06 Aug 2024 15:16:57 GMT
---

<h1 id="linkedlist">LinkedList</h1>
<p>링크드리스트는 리스트의 구현체로 비순차적인 데이터의 추가 및 삭제에 용이한 자료구조다. 다만, 인덱스 기반 조회는 O(N)의 시간 복잡도를 가진다는 점이 단점이다. </p>
<h1 id="listiterator">.listIterator</h1>
<p>링크드리스트의 <code>.listIterator</code> 메서드를 사용해보자.</p>
<p>이 메서드는 <code>int index</code>를 인자로 받아서 <code>index</code> 인덱스부터 시작하는 <code>ListIterator</code> 타입을 반환한다. </p>
<h1 id="listiterator의-메서드">ListIterator의 메서드</h1>
<h2 id="1-hasnext-hasprevious">1. hasNext, hasPrevious</h2>
<ol>
<li><code>.hasNext()</code></li>
</ol>
<p>boolean 값을 리턴하는 메서드로, 리스트의 앞에서 뒷쪽으로 순회할 때 다음에 값이 있는지 확인할 수 있다.</p>
<ol start="2">
<li><code>.hasPrevious()</code></li>
</ol>
<p>boolean 값을 리턴하는 메서드로, 리스트의 뒤에서 앞쪽으로 순회할 때 이 값 이전에 값이 있는지 확인할 수 있다.</p>
<h2 id="2-next-nextindex">2. next, nextIndex</h2>
<ol>
<li><code>.next()</code></li>
</ol>
<p>리스트의 제네릭 타입을 반환하는 메서드로, 리스트에 다음 순서로 있는 요소를 반환하고 커서의 포지션을 다음으로 옮긴다. </p>
<ol start="2">
<li><code>.nextIndex()</code></li>
</ol>
<p>다음 순서로 있는 요소의 인덱스를 반환한다. 반환 타입은 int다. </p>
<h2 id="3-previous-previousindex">3. previous, previousIndex</h2>
<ol>
<li><code>.previous()</code></li>
</ol>
<p>리스트의 제네릭 타입을 반환하는 메서드로, 리스트에 이전 순서로 있는 요소를 반환하고 커서의 포지션을 이전으로 옮긴다. </p>
<ol start="2">
<li><code>.previousIndex()</code></li>
</ol>
<p>이전 순서로 있는 요소의 인덱스를 반환한다. 반환 타입은 int다. </p>
<h2 id="4-add-remove">4. add, remove</h2>
<ol>
<li><code>add(E e)</code></li>
</ol>
<p>아무것도 반환하지 않는다. 현재 커서의 위치에 값을 추가한다.</p>
<ol start="2">
<li><code>remove()</code></li>
</ol>
<p>가장 최근 연산에서 <code>next()</code> 또는 <code>previous()</code>로 인해 리턴된 값을 제거한다. 반환 값은 없다. </p>
<h1 id="listiterator를-활용해-키로거-백준-5397을-풀어보자">ListIterator를 활용해 &lt;키로거&gt; 백준 #5397을 풀어보자</h1>
<p>&lt;키로거&gt; 문제는 단순 구현이나 <code>ArrayDeque</code>, <code>Queue</code>, <code>Stack</code> 등을 활용해서도 풀 수 있지만, 메모리 사용량과 시간 면 모두에 있어서 <code>ListIterator</code>를 사용하는 것이 가장 효율적이다.</p>
<p><img alt="" src="https://velog.velcdn.com/images/becooq81/post/0899ef60-65dc-44ea-8488-b505c9625ef6/image.png" /></p>
<p>위 사진에서 위에서부터 순서대로 <code>ListIterator</code>, 이중 <code>ArrayDeque</code>, 그리고 단순 구현으로 풀었을 때의 메모리와 시간을 확인할 수 있다. </p>
<h2 id="문제-해결-로직">문제 해결 로직</h2>
<p>특수문자 (<code>&lt;</code>, <code>&gt;</code>, <code>-</code>)를 제외하고는 모두 링크드리스트에 더하면 된다. 특수 케이스를 다뤄보자. </p>
<ol>
<li><code>&lt;</code>은 iterator의 커서를 왼쪽으로 한 칸 움직인다. </li>
</ol>
<p>커서를 움직일 글자가 있는지 여부를 확인한 후 연산을 해야 한다.
왼쪽에 커서가 이동할 글자가 있는지 <code>hasPrevious()</code>로 확인한 다음, <code>previous()</code>를 호출해서 커서를 이동시킨다. </p>
<ol start="2">
<li><code>&gt;</code>은 iterator의 커서를 오른쪽으로 한 칸 움직인다. (커서를 움직일 글자가 있으면)</li>
</ol>
<p>이번에는 오른쪽에 커서가 이동할 글자가 있는지 확인하기 위해 <code>hasNext()</code>를 호출한다. 그 다음 <code>next()</code>로 커서를 이동시킨다. </p>
<ol start="3">
<li><code>-</code>은 iterator의 커서를 왼쪽으로 한 칸 움직인 다음 글자를 제거한다. </li>
</ol>
<p>커서의 왼쪽의 글자를 pop해야 하기 때문에 왼쪽에 글자가 있는지 <code>hasPrevious()</code>로 확인한다. 
<code>remove()</code>는 가장 최근에 <code>previous()</code> 또는 <code>next()</code>로 리턴된 값을 제거하기 때문에 <code>previous()</code>로 커서 왼쪽의 값을 리턴한 후, <code>remove()</code>를 호출한다. </p>
<h2 id="코드">코드</h2>
<p><a href="https://github.com/becooq81/Algorithms/blob/main/Java/%EB%B0%B1%EC%A4%80/Silver/5397.%E2%80%85%ED%82%A4%EB%A1%9C%EA%B1%B0/%ED%82%A4%EB%A1%9C%EA%B1%B0.java">백준 #5397 키로거</a></p>
<hr />
<p><a href="https://docs.oracle.com/javase/8/docs/api/java/util/ListIterator.html">https://docs.oracle.com/javase/8/docs/api/java/util/ListIterator.html</a></p>