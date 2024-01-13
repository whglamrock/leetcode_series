
# O(n) solution: see: https://leetcode.com/problems/k-th-symbol-in-grammar/solutions/4205730/100-easy-iterative-approach-explained-intuition/
# 1) 0 -> 01 -> 0110 -> 0110 1001 -> 0110 1001 1001 0110 -> 0110 1001 1001 0110 1001 0110 0110 1001
# -> 0110 1001 1001 0110 1001 0110 0110 1001 1001 0110 0110 1001 0110 1001 1001 0110
# 2) You can see that the first half of each row == row - 1, and the second half is the reverse of 1st half
# 3) for kth element, if k > len(row) // 2, it's the reverse value of (k - len(row) // 2)th element.
# 4) if k < len(row) // 2, it's the kth element in row - 1. So we keep decreasing n by half until row 1 == [0]
class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        # check if k == the value of the first bit
        areValuesSame = True
        # total num of elements in the nth row is 2 ^ (n - 1)
        n = 2 ** (n - 1)

        while n > 1:
            n //= 2
            # k is in the second half
            if k > n:
                k -= n
                areValuesSame = not areValuesSame

        return 0 if areValuesSame else 1


print(Solution().kthGrammar(30, 1035))
