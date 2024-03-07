from typing import List

# remember this setup. Only consider the first half. See idea from: https://leetcode.com/problems/find-palindrome-with-fixed-length/solutions/1886915/formula/
class Solution:
    def kthPalindrome(self, queries: List[int], intLength: int) -> List[int]:
        start = 10 ** ((intLength + 1) // 2 - 1)
        end = 10 ** ((intLength + 1) // 2) - 1
        ans = []
        for query in queries:
            if start + query - 1 > end:
                ans.append(-1)
                continue
            leftHalf = str(int(start + query - 1))
            rightHalf = leftHalf[::-1]
            if intLength % 2 != 0:
                rightHalf = rightHalf[1:]
            ans.append(int(leftHalf + rightHalf))

        return ans
