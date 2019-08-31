
For each topic/special data structure, the typical use cases are summaized here

##### Binary Index Tree
* O(logN) time for update and getPrefixSum for an array
* count in an array, the numbers smaller/bigger than a number on its left/right. 
* Example question: 
    * count of smaller/bigger numbers on the left/right: [lc315: count of smaller numbers after self](https://leetcode.com/problems/count-of-smaller-numbers-after-self/)
    * typical prefix sum: [lc327: count of range sum](https://leetcode.com/problems/count-of-range-sum/)

##### Dynamic Programming
Usually (or almost 95% of the case) what `dp[i][j]` means should be exactly same as what the question is asking for. In some case, we may need multiple dp array to track the previous state, depending on what the question is asking for.
* Typical one 2-D dp array question:
    * [lc10: regular expression matching](https://leetcode.com/problems/regular-expression-matching/)
    * [lc97: Interleaving String](https://leetcode.com/problems/interleaving-string/)
    * [lc188: best time to sell stock with k transactions](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/)
* Multiple dp array is involved:
    * [lc85: Maximal Rectangle](https://leetcode.com/problems/maximal-rectangle/)
    


