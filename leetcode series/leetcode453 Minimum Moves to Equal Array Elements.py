# suppose we take m steps. sumvalue + m * (n - 1) = x * n = (minNum + m) * n
#   Thus, m = (sumvalue - n * minNum) / n

class Solution(object):
    def minMoves(self, nums):

        sumvalue = sum(nums)
        n = len(nums)
        minNum = min(nums)

        return sumvalue - n * minNum


# Finally, all numbers will reach to some number x. The key is to understand why x = minNum + m.
# 1) Before all numbers reach to x, there is at least one number bigger than the minNum;
# 2) After every add one operation, there is always a number that still bigger than it;
# 3) So, the initial minimum number will always remain minimum
