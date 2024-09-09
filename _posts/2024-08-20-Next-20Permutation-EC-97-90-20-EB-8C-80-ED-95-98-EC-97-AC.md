---
title: "Next Permutation에 대하여"
date: 2024-08-20T07:20:24+00:00
---

<h1 id="permutation">Permutation</h1>
<p>알고리즘에서 재귀적으로 구현할 수 있는 순열은 O(N!)이라는 어마어마한 시간복잡도를 가진다. N이 10을 넘어가면 순열을 사용할 수 있을지 다시 한번 고민해봐야 한다.</p>
<p>전체 순열을 구할 필요 없이, 현재 순열의 다음 순서인 순열만 필요하다면 Next Permutation 알고리즘을 사용하여 구하면 시간복잡도를 현저히 낮출 수 있다. </p>
<h1 id="next-permutation">Next Permutation</h1>
<p>다음 순열 알고리즘의 '다음'은 사전순에 있어서 다음을 의미한다</p>
<h2 id="1-알고리즘의-이해">1. 알고리즘의 이해</h2>
<p>다음 순열을 찾기 위한 알고리즘은 다음과 같다</p>
<h4 id="1-배열의-마지막-요소부터-순회하며-사전-순서를-따르는-첫-인덱스-즉-pivot을-찾는다">1. 배열의 마지막 요소부터 순회하며 사전 순서를 따르는 첫 인덱스, 즉 pivot을 찾는다.</h4>
<p>사전 순서를 따르면, <code>arr[i] &lt;= arr[i+1]</code>의 규칙을 따라야 한다. </p>
<h4 id="2-pivot-인덱스가-유효한-값인지-확인한다">2. pivot 인덱스가 유효한 값인지 확인한다</h4>
<p>(1)의 결과인 인덱스가 유효하지 않을 수 있다. 이 경우에는 전체적으로 스왑이 이뤄져야 한다.</p>
<p>pivot 인덱스가 유효하면 (3)을 진행한다.
유효하지 않다면 </p>
<h4 id="3-마지막-요소부터-순회하며--pivot보다-큰-요소-successor를-찾는다">3. 마지막 요소부터 순회하며 = pivot보다 큰 요소, successor를 찾는다</h4>
<h4 id="4-pivot과-successor를-스왑한다">4. pivot과 successor를 스왑한다</h4>
<h4 id="5-pivot1-인덱스부터-끝까지-reverse한다">5. pivot+1 인덱스부터 끝까지 reverse한다</h4>
<h1 id="2-구현">2. 구현</h1>
<p>알고리즘에 따르면 우리가 구현해야 하는 것은 크게 세 부분으로 나눌 수 있다. </p>
<h4 id="1-pivot을-찾는-코드">1. pivot을 찾는 코드</h4>
<pre><code class="language-java">int i = nums.length - 2;
while (i &gt;= 0 &amp;&amp; nums[i] &gt;= nums[i + 1]) {
    i--;
}</code></pre>
<h4 id="1-1-pivot을-찾았다면-successor를-찾는-코드">1-1. pivot을 찾았다면 successor를 찾는 코드</h4>
<pre><code class="language-java">if (i &gt;= 0) {
    int j = nums.length - 1;
    while (nums[j] &lt;= nums[i]) {
        j--;
    }
    swap(nums, i, j);
}</code></pre>
<p>이 때 사용될 스왑 코드는 (2)에서 구현한다</p>
<h4 id="2-스왑하는-코드">2. 스왑하는 코드</h4>
<pre><code class="language-java">private static void swap(int[] nums, int i, int j) {
    int temp = nums[i];
    nums[i] = nums[j];
    nums[j] = temp;
}</code></pre>
<p>스왑당할 값을 <code>temp</code>에 저장해두고 바꿔치기한다</p>
<h4 id="3-reverse하는-코드">3. reverse하는 코드</h4>
<pre><code class="language-java">private static void reverse(int[] nums, int start) {
    int i = start, j = nums.length - 1;
    while (i &lt; j) {
        swap(nums, i, j);
        i++;
        j--;
    }
}</code></pre>
<h1 id="전체-코드">전체 코드</h1>
<pre><code class="language-java">import java.util.Arrays;

public class NextPermutation {
    public static void nextPermutation(int[] nums) {
        // 마지막 요소부터 순회하며 사전순서를 따르는 첫 요소를 찾습니다
        int i = nums.length - 2;
        while (i &gt;= 0 &amp;&amp; nums[i] &gt;= nums[i + 1]) {
            i--;
        }
        // pivot을 찾았으면, 이보다 큰 값을 뒷쪽에서 찾습니다
        if (i &gt;= 0) {
            int j = nums.length - 1;
            while (nums[j] &lt;= nums[i]) {
                j--;
            }
            // 두 요소를 스왑합니다
            swap(nums, i, j);
        }
        // i+1부터 끝까지의 요소를 역순으로 바꿔서 다음 순열을 구합니다
        reverse(nums, i + 1);
    }

    private static void swap(int[] nums, int i, int j) {
        int temp = nums[i];
        nums[i] = nums[j];
        nums[j] = temp;
    }

    private static void reverse(int[] nums, int start) {
        int i = start, j = nums.length - 1;
        while (i &lt; j) {
            swap(nums, i, j);
            i++;
            j--;
        }
    }

    public static void main(String[] args) {
        int[] nums = { 3, 2, 1 };
        nextPermutation(nums);
        System.out.println(Arrays.toString(nums));
    }
}</code></pre>
<hr />
<p><a href="https://www.geeksforgeeks.org/next-permutation/">https://www.geeksforgeeks.org/next-permutation/</a></p>