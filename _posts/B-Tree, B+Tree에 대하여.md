<h1 id="binary-search-tree">Binary Search Tree</h1>
<hr />
<p>Definition: a hierarchical data structure (tree) in which each node has at most 2 children</p>
<ul>
<li>A node's left subtree has values less than the node's value</li>
<li>A node's right subtree has values greater than the node's value</li>
</ul>
<p>BST enables efficient search for values since all values are sorted into the tree. 
However, upon insertion and deletion operations, the tree must rebalance each time, resulting in inefficient performances. </p>
<h1 id="m-way-search-tree">M-Way Search Tree</h1>
<hr />
<p>Multi-level indexing attempts to manage multiple indexes, which appeared with larger datasets. </p>
<ul>
<li>Another level of indexing: The new index stores a pointer to each block of the first level index table</li>
</ul>
<ul>
<li>uses a hierarchy of index structures to efficiently access data</li>
<li>keeps a tree balanced by storing more than 1 key per node <ul>
<li>Hence, a tree will always be perfect (but not necessarily binary)</li>
</ul>
</li>
</ul>
<p>M-way search tree is a common multi-level indexing structure that allows more than two children per node, more specifically M-1 to 2M-1 children (M &gt;= 1).</p>
<p>Unfortunately, this restriction in number of trees means that the tree requires restructuring upon insertion and deletion operations.</p>
<h1 id="b-tree">B-tree</h1>
<hr />
<p><img alt="" src="https://velog.velcdn.com/images/becooq81/post/04e0f62a-8712-4385-b559-74f7161a5804/image.png" /></p>
<p>A B-tree addresses the shortcomings of M-way search trees in cases of frequent insertions and deletions.</p>
<p>Definition: a <strong>balanced</strong> tree structure that </p>
<ul>
<li><strong>balanced</strong> height: all leaf nodes are at the same level<ul>
<li>self-balancing</li>
<li>enables predictable and efficient search operations</li>
</ul>
</li>
<li>provides sorted data</li>
<li>allows searches, sequential access, insertions/deletions in sorted order</li>
<li>maintains a BST quality of having a node's left subtree as values less than node and its right subtree as values greater than node</li>
<li>but allows more than 2 children </li>
</ul>
<p>Downsides</p>
<ul>
<li>requires additional storage space for creating and maintaining a B-tree</li>
<li>restructuring a B-tree upon insertions and deletions may cause performance issues</li>
</ul>
<h1 id="b-tree-1">B+ tree</h1>
<hr />
<p>The key difference between a B-tree and a B+ tree is how data is stored. The fact that B-trees store data in internal and leaf nodes whereas <strong>B+ trees store data only in leaf nodes</strong> result in the following differences as well.</p>
<ol>
<li><p><strong>Data pointer storage</strong></p>
<ul>
<li>All internal and leaf nodesof B-trees have data pointers</li>
<li>Only leaf nodes of B+trees have data pointers</li>
</ul>
</li>
<li><p><strong>Redundant keys</strong></p>
<ul>
<li>B-tree does not have duplicates of keys<ul>
<li>B+tree has duplicate keys since all nodes are present at a leaf node.</li>
</ul>
</li>
</ul>
</li>
<li><p><strong>Search complexity</strong></p>
<ul>
<li>B+ tree has simplified search process because all data is found in leaf nodes</li>
<li>B+ tree allows sequential search due to linked list nature of leaf nodes</li>
</ul>
</li>
<li><p><strong>Range queries</strong></p>
<ul>
<li>Leaf nodes of a B+ tree are linearly connected, improving range-query performances</li>
</ul>
</li>
<li><p><strong>Balancing</strong></p>
<ul>
<li>Leaf-only data structures allows B+ trees to be more balanced</li>
</ul>
</li>
</ol>
<hr />
<p>References: </p>
<ul>
<li><a href="https://www.linkedin.com/pulse/deep-understanding-b-tree-indexing-sohel-rana/">https://www.linkedin.com/pulse/deep-understanding-b-tree-indexing-sohel-rana/</a></li>
<li><a href="https://shambhavishandilya.medium.com/b-tree-indexing-basics-explained-%EF%B8%8F-56ae0bda46c4">https://shambhavishandilya.medium.com/b-tree-indexing-basics-explained-%EF%B8%8F-56ae0bda46c4</a></li>
<li><a href="https://builtin.com/data-science/b-tree-index">https://builtin.com/data-science/b-tree-index</a></li>
<li><a href="https://www.geeksforgeeks.org/difference-between-b-tree-and-b-tree/">https://www.geeksforgeeks.org/difference-between-b-tree-and-b-tree/</a></li>
</ul>