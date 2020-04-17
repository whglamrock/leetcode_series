
For each topic/special data structure, the typical use cases are summaized here

##### Binary Index Tree
* O(logN) time for update and getPrefixSum for an array
* count in an array, the numbers smaller/bigger than a number on its left/right. 
* Example question: 
    * count of smaller/bigger numbers on the left/right: [lc315. count of smaller numbers after self](https://leetcode.com/problems/count-of-smaller-numbers-after-self/), [lc493. Reverse Pairs](https://leetcode.com/problems/reverse-pairs/)
    * typical prefix sum: [lc327. count of range sum](https://leetcode.com/problems/count-of-range-sum/)


##### Dynamic Programming
Usually (or almost 95% of the case) what `dp[i][j]` means should be exactly same as what the question is asking for. In some case, we may need multiple dp array to track the previous state. 
* Typical one 2-D dp array question:
    * [lc10. regular expression matching](https://leetcode.com/problems/regular-expression-matching/)
    * [lc97. Interleaving String](https://leetcode.com/problems/interleaving-string/)
    * [lc188. best time to sell stock with k transactions](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/)
    * [lc72. Edit Distance](https://leetcode.com/problems/edit-distance/)
    * classic knapsack problem: [lc518. Coin Change 2](https://leetcode.com/problems/coin-change-2/), notice how we use `dp[i][j]`'s definition to avoid duplicates of combination
* Multiple dp array is involved:
    * [lc85. Maximal Rectangle](https://leetcode.com/problems/maximal-rectangle/)
* A very special question where the only idea needs us to starts from final state (top-down instead of bottom-up): [lc174. Dungeon Game](https://leetcode.com/problems/dungeon-game/); when you find it's hard to do bottom up, try the top down idea
* When you don't necessarily need a dp array, but multiple state variables: [lc309. Best Time to Buy and Sell Stock with Cooldown](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/), [lc714. Best Time to Buy and Sell Stock with Transaction Fee](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/)


##### Merge Sort
Merge sort usually should not be needed, but it is needed the question is likely to a hard one.
* [lc327. Count of Range Sum](https://leetcode.com/problems/count-of-range-sum/)


##### Backtracking
* Some questions with backtracking tag sometimes can be solved in top-down DFS way. E.g., [lc140. Word Break II](https://leetcode.com/problems/word-break-ii/)
* Textbook backtracking questions: [lc46. Permutations](https://leetcode.com/problems/permutations), [lc37. Sudoku Solver](https://leetcode.com/problems/sudoku-solver)


##### Binary Search
* Usually the while loop condition, initial range, how we move the index are two combinations: `l, r = 0, n & while l < r & r = m & l = m + 1` or `l, r = 0, n - 1 & while l <= r & r = m - 1 & l = m + 1`. There are some special cases, e.g., [lc4. Median of Two Sorted Arrays](https://leetcode.com/problems/median-of-two-sorted-arrays/)
* Classic Binary search question with easy to fall trap: [lc33. Search in Rotated Sorted Array](https://leetcode.com/problems/search-in-rotated-sorted-array/)
* Atypical question where we don't search in a range: [lc29. Divide Two Integers](https://leetcode.com/problems/divide-two-integers/submissions/)
* The sorted list is formed in a very un-straightforward way (not original nums or prefix sum):
    * [lc300. Longest Increasing Subsequence](https://leetcode.com/problems/longest-increasing-subsequence/)
* In most cases we would always make m = (l + r) / 2 but there's also situation when we make m = (l + r + 1) / 2: [lc34. Find First and Last Position of Element in Sorted Array](https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/submissions/)
* An atypical binary question where searched range is not sorted and using prefixSum won't work: [lc162. Find Peak Element](https://leetcode.com/problems/find-peak-element/)


##### Topology Sort
* Textbook topology sort questions: [lc269. Alien Dictionary](https://leetcode.com/problems/alien-dictionary/), [lc207. Course Schedule](https://leetcode.com/problems/course-schedule/), [lc210. Course Schedule II](https://leetcode.com/problems/course-schedule-ii/) 
* A hard version: [lc1203. Sort Items by Groups Respecting Dependencies](https://leetcode.com/problems/sort-items-by-groups-respecting-dependencies/) where it's more convenient to use an additional "indegree" variable to store the node to degree mapping. "Degree" means how many direct children this node has  


##### Union Find
Note that when we do path compression with the "find" method, the parent of a union will very likely change. So union find is not very appropriate, or more error prone to solving questions like "find number of disconnected parts in a disconnected graph". 
* A textbook unionFind question that includes detecting circle in a graph: [lc684. Redundant Connection](https://leetcode.com/problems/redundant-connection/)
* A typical question that is best/easiest to be solved with union find: [lc261. Graph Valid Tree](https://leetcode.com/problems/graph-valid-tree/). Follow up: [lc685. Redundant Connection II](https://leetcode.com/problems/redundant-connection-ii/), which needs some tricky pre-processing before we can use union find.
* [lc305. Number of Islands II](https://leetcode.com/problems/number-of-islands-ii/), the harder version which practically can only be solved by UnionFind


##### Graph
some of the questions under this topic are actually covered by topology sort & union find. so only list few typical ones here
* For Euler path algorithm: [lc332. Reconstruct Itinerary](https://leetcode.com/problems/reconstruct-itinerary/)
* "union find alike" graph question: [lc399. Evaluate Division](https://leetcode.com/problems/evaluate-division/)
* A typical Djikstra algorithm question solved with heapq: [lc743. Network Delay Time](https://leetcode.com/problems/network-delay-time/)


##### DFS/BFS
most of the DFS questions can also be solved with BFS
* Textbook question that must be remembered and also be used as template: [lc200. Number of Islands](https://leetcode.com/problems/number-of-islands/)
* Questions that can also be solved with union find: [lc947. Most Stones Removed with Same Row or Column](https://leetcode.com/problems/most-stones-removed-with-same-row-or-column/), [lc924. Minimize Malware Spread](https://leetcode.com/problems/minimize-malware-spread/)
* A "DP alike" question but more practical to be solved with DFS: [lc741. Cherry Pickup](https://leetcode.com/problems/cherry-pickup/)


##### Greedy
* A hard, graph related greedy question that needs solid proof: [lc765. Couples Holding Hands](https://leetcode.com/problems/couples-holding-hands/)
* The greedy idea is not very obvious and the solution thought isn't easy to explain: [lc1130. Minimum Cost Tree From Leaf Values](https://leetcode.com/problems/minimum-cost-tree-from-leaf-values/)


##### Two pointers
* Most classic fast & slow 2 pointer question: [lc141. Linked List Cycle](https://leetcode.com/problems/linked-list-cycle/), follow-up: [lc142. Linked List Cycle II](https://leetcode.com/problems/linked-list-cycle-ii/)
* A typical question that shares the fast & slow 2 pointer idea: [lc 287. Find the Duplicate Number](https://leetcode.com/problems/find-the-duplicate-number/); for this one, the O(1) extra space requirement will make it a hard question because you have to think of using the value -> index mapping to form a linked list
