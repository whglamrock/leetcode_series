
For each topic/special data structure, the typical use cases are summaized here

##### Binary Index Tree
* O(logN) time for update and getPrefixSum for an array
* count in an array, the numbers smaller/bigger than a number on its left/right. 
* Example question: 
    * count of smaller/bigger numbers on the left/right: [lc315. count of smaller numbers after self](https://leetcode.com/problems/count-of-smaller-numbers-after-self/), [lc493. Reverse Pairs](https://leetcode.com/problems/reverse-pairs/)
    * typical prefix sum: [lc327. count of range sum](https://leetcode.com/problems/count-of-range-sum/)


##### Dynamic Programming
Usually (or almost 95% of the case) what `dp[i][j]` means should be exactly same as what the question is asking for. In some case, we may need multiple dp array to track the previous state, depending on what the question is asking for.
* Typical one 2-D dp array question:
    * [lc10. regular expression matching](https://leetcode.com/problems/regular-expression-matching/)
    * [lc97. Interleaving String](https://leetcode.com/problems/interleaving-string/)
    * [lc188. best time to sell stock with k transactions](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/)
    * [lc72. Edit Distance](https://leetcode.com/problems/edit-distance/)
    * 
* Multiple dp array is involved:
    * [lc85: Maximal Rectangle](https://leetcode.com/problems/maximal-rectangle/)
    

##### Merge Sort
Merge sort usually should not be needed, but it is needed the question is likely to a hard one.
* [lc327: Count of Range Sum](https://leetcode.com/problems/count-of-range-sum/)


##### Backtracking
Some questions with backtracking tag sometimes can be solved in top-down DFS way. E.g., [lc140. Word Break II](https://leetcode.com/problems/word-break-ii/)


##### Binary Search
* Usually the while loop condition, initial range, how we move the index are two triplets: `l, r = 0, n & while l < r & r = m` or `l, r = 0, n - 1 & while l <= r & r = m - 1`. There are some special cases, e.g., [lc4. Median of Two Sorted Arrays](https://leetcode.com/problems/median-of-two-sorted-arrays/)
* Classic Binary search question with east to fall trap: [lc33. Search in Rotated Sorted Array](https://leetcode.com/problems/search-in-rotated-sorted-array/)
* Non-typical question where we don't search in a range: [lc29. Divide Two Integers](https://leetcode.com/problems/divide-two-integers/submissions/)
* The sorted list is formed in a very un-straightforward way (not original nums or prefix sum):
    * [lc300. Longest Increasing Subsequence](https://leetcode.com/problems/longest-increasing-subsequence/)
* In most cases we would always make m = (l + r) / 2 but there's also situation when we make m = (l + r + 1) / 2: [lc34. Find First and Last Position of Element in Sorted Array](https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/submissions/)

##### Topology Sort


##### Union Find


##### Graph

##### Two pointers
* Most classic fast & slow 2 pointer question: [lc141. Linked List Cycle](https://leetcode.com/problems/linked-list-cycle/), follow-up: [lc142. Linked List Cycle II](https://leetcode.com/problems/linked-list-cycle-ii/)
* A typical question that shares the fast & slow 2 pointer idea: [lc 287. Find the Duplicate Number](https://leetcode.com/problems/find-the-duplicate-number/)
