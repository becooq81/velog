---
title: "[JAVA] TreeMap을 사용해보자"
date: Thu, 01 Aug 2024 06:27:03 GMT
---

<h1 id="treemapk-v">TreeMap&lt;K, V&gt;</h1>
<p>Java의 TreeMap은 Map 인터페이스, NavigableMap 인터페이스와 AbstractMap 클래스를 구현한다</p>
<h3 id="특징">특징</h3>
<ul>
<li>Key 값 기준으로 자연적인 순서(오름차순)로 정렬한다<ul>
<li><code>Comparator</code>를 도입하여 정렬 기준을 재정의할 수 있다</li>
</ul>
</li>
<li>Red-Black 트리 (자가 균형 이진 탐색 트리의 종류)로 구현되어 있다<ul>
<li>즉, 데이터의 추가, 삭제, 조회의 시간 복잡도가 O(log N)으로 우수하다</li>
</ul>
</li>
</ul>
<h3 id="메서드">메서드</h3>
<h4 id="1-생성자">1. 생성자</h4>
<pre><code class="language-java">TreeMap&lt;Integer, Integer&gt; treeMap = new TreeMap&lt;&gt;();</code></pre>
<p>정렬 기준을 재정의하고 싶은 경우 <code>()</code> 안에 Comparator를 도입하면 된다</p>
<h4 id="2-데이터-추가">2. 데이터 추가</h4>
<pre><code class="language-java">treeMap.put(key, value);</code></pre>
<h4 id="3-데이터-삭제">3. 데이터 삭제</h4>
<p>key 기준 제거</p>
<pre><code class="language-java">treeMap.remove(key);</code></pre>
<p>최소 key 값의 entry 제거: <code>Map.Entry&lt;K, V&gt;</code>를 리턴한다</p>
<pre><code class="language-java">treeMap.pollFirstEntry();</code></pre>
<p>최대 key 값의 entry 제거: <code>Map.Entry&lt;K, V&gt;</code>를 리턴한다</p>
<pre><code class="language-java">treeMap.pollLastEntry();</code></pre>
<h4 id="4-데이터-조회">4. 데이터 조회</h4>
<p>특정 key가 있는지 여부 조회</p>
<pre><code class="language-java">treeMap.containsKey(key); // boolean 값 리턴</code></pre>
<p>특정 key의 value 조회</p>
<pre><code class="language-java">treeMap.get(key);</code></pre>
<p>특정 value가 있는지 여부 조회</p>
<pre><code class="language-java">treeMap.containsValue(value); 
// 1개 이상의 key가 해당 value를 가지면 true</code></pre>
<h4 id="5-최솟값-최댓값-조회">5. 최솟값, 최댓값 조회</h4>
<p>최소/최대 키만 조회</p>
<pre><code class="language-java">treeMap.firstKey(); // 기본적으로 오름차순 정렬이라 최소값 리턴
treeMap.lastKey(); // 최대값 리턴</code></pre>
<p>최소/최대 키 값의 entry 조회</p>
<pre><code class="language-java">treeMap.firstEntry(); 
treeMap.lastEntry();</code></pre>
<h4 id="6-부분-조회">6. 부분 조회</h4>
<pre><code class="language-java">treeMap.subMap(startKey, endKey);</code></pre>
<p>startKey부터 endKey 전까지의 범위에 포함되는 key들의 map을 리턴한다</p>
<h4 id="7-내림차순-전체-조회">7. 내림차순 전체 조회</h4>
<p>전체 맵의 내림차순</p>
<pre><code class="language-java">NavigableMap&lt;Integer, Integer&gt; reversedTreeMap = treeMap.descendingMap();</code></pre>
<p>key 값들의 내림차순</p>
<pre><code class="language-java">NavigableSet&lt;Integer&gt; reversedKeySet = treeMap.descendingKeySet();</code></pre>
<h4 id="8-이외-유용한-메서드">8. 이외 유용한 메서드</h4>
<ul>
<li><p><code>Map.Entry&lt;K, V&gt; ceilingEntry(K key)</code> : 인수 키 이상인 키 값 중 최소 값의 entry를 리턴한다. 만족하는 entry가 없을 경우 null을 리턴한다</p>
</li>
<li><p><code>Map.Entry&lt;K, V&gt; higherEntry(K key)</code> : 인수 키 초과인 키 값 중 최소 값의 entry를 리턴한다. 만족하는 entry가 없을 경우 null 리턴한다</p>
</li>
<li><p><code>SortedMap&lt;K, V&gt; headMap(K toKey)</code>: 인수 키 값보다 작은 키의 key-value 집합을 맵으로 리턴한다. <code>boolean inclusive</code> 인수를 추가할 수 있다</p>
</li>
</ul>
<h1 id="활용-문제-백준7662">활용 문제 백준#7662</h1>
<p>골드4인 문제지만 TreeMap을 사용하면 아주 간단하게 풀 수 있다. </p>
<h3 id="문제-이해">문제 이해</h3>
<p>3가지 연산이 가능하다</p>
<ol>
<li>데이터의 삽입</li>
<li>현재 데이터 집합의 최솟값 제거</li>
<li>현재 데이터 집합의 최댓값 제거</li>
</ol>
<h3 id="해결-방안">해결 방안</h3>
<p>최솟값과 최댓값를 효율적으로 제거하기 위해서 우선순위큐를 2개 두고, 현재 제거되지 않은 데이터에 대한 맵을 유지하는 방식으로도 이 문제를 풀 수 있지만, TreeMap을 활용하면 더 간단하게 풀 수 있다. </p>
<p>최솟값은 <code>.firstKey()</code>, 최댓값은 <code>.lastKey()</code>를 활용해서 조회하고, 해당 키의 value 값이 0이면 맵에서 제거하면 된다. 어떤 값이 실제로는 제거되어야 하는데 아직 집합에 남아있는 잔실수를 방지할 수 있다.</p>
<p>초반에 설명했듯이 데이터의 추가, 삭제, 조회 연산 등이 O(log N)으로 효율적이기 때문에 시간 초과 또한 걸리지 않는다</p>
<h3 id="풀이-코드">풀이 코드</h3>
<p><a href="https://github.com/becooq81/algorithms/blob/main/Java/%EB%B0%B1%EC%A4%80/Gold/7662.%E2%80%85%EC%9D%B4%EC%A4%91%E2%80%85%EC%9A%B0%EC%84%A0%EC%88%9C%EC%9C%84%E2%80%85%ED%81%90/%EC%9D%B4%EC%A4%91%E2%80%85%EC%9A%B0%EC%84%A0%EC%88%9C%EC%9C%84%E2%80%85%ED%81%90.java">이중 우선순위 큐 #7662 풀이 코드</a></p>
<hr />
<p>출처:
<a href="https://www.geeksforgeeks.org/treemap-in-java/">https://www.geeksforgeeks.org/treemap-in-java/</a>
<a href="https://docs.oracle.com/javase/8/docs/api/java/util/TreeMap.html">https://docs.oracle.com/javase/8/docs/api/java/util/TreeMap.html</a></p>