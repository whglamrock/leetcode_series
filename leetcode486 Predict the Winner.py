
# a standard minmax solution.
# for MIT OCW: https://www.youtube.com/watch?v=Tw1k46ywN6E&feature=youtu.be&list=PLUl4u3cNGP6317WaSNfmCvGym2ucw3oGp&t=3622

class Solution(object):
    def PredictTheWinner(self, nums):

        n = len(nums)

        # the 'n % 2 == 0' check can rule out half of the conditions
        #if n % 2 == 0:
            #return True

        self.dp = {}
        self.nums = nums
        myBest = self.helper(0, n - 1)
        return 2 * myBest >= sum(nums)

    def helper(self, i, j):

        if i > j:
            return 0
        if (i, j) in self.dp:
            return self.dp[(i, j)]

        # i + 1 to j are left over
        a = self.nums[i] + min(self.helper(i + 1, j - 1), self.helper(i + 2, j))
        # i to j - 1 are left over
        b = self.nums[j] + min(self.helper(i + 1, j - 1), self.helper(i, j - 2))
        self.dp[(i, j)] = max(a, b)

        return self.dp[(i, j)]



'''
# a top - down dp solution
# see explanation for the logic: https://discuss.leetcode.com/topic/76312/java-1-line-recursion-solution/2

class Solution(object):
    def PredictTheWinner(self, nums):

        n = len(nums)
        self.nums = nums
        self.memo = {}

        return self.dp(0, n - 1) >= 0

    # due to the mechanism of dp, there is no need to check if lo > hi
    def dp(self, lo, hi):

        if (lo, hi) not in self.memo:
            if lo == hi:
                self.memo[(lo, hi)] = self.nums[lo]
            else:
                self.memo[(lo, hi)] = max(self.nums[lo] - self.dp(lo + 1, hi), self.nums[hi] - self.dp(lo, hi - 1))

        return self.memo[(lo, hi)]
'''



'''
# the following solution actually avoids the minmax logic

class Solution(object):
    def PredictTheWinner(self, nums):

        self.nums = nums
        return self.first(0, len(nums) - 1, 0, 0)

    def first(self, lo, hi, s1, s2):
        #print lo, hi, s1, s2
        if lo > hi:
            return s1 >= s2

        # in two possibilities, if there is one in which player2 can't win, the player1 can choose it
        return (not self.second(lo + 1, hi, s1 + self.nums[lo], s2)) or (not self.second(lo, hi - 1, s1 + self.nums[hi], s2))

    def second(self, lo, hi, s1, s2):
        #print lo, hi, s1, s2
        if lo > hi:
            return s1 < s2

        return (not self.first(lo + 1, hi, s1, s2 + self.nums[lo])) or (not self.first(lo, hi - 1, s1, s2 + self.nums[hi]))
'''