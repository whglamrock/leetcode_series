
# the below solution got stupid TLE. This type of match problem is just so fucking stupid and meaningless

class Solution(object):
    def consecutiveNumbersSum(self, n):
        """
        :type n: int
        :rtype: int
        """
        ans = 1  # itself counts as 1
        for i in range(1, n // 2 + 1):
            for j in range(2, n):
                if (i + (i + j - 1)) * j / 2 == n:
                    ans += 1

        return ans


Sol = Solution()
print(Sol.consecutiveNumbersSum(5))
print(Sol.consecutiveNumbersSum(9))
print(Sol.consecutiveNumbersSum(1234))
