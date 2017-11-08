
# basic DFS solution with memoization, the parameter being passed is a list
#   containing all available numbers instead of used status list of each number (to avoid putback)

class Solution(object):
    def canIWin(self, maxChoosableInteger, desiredTotal):

        if (1 + maxChoosableInteger) * maxChoosableInteger / 2 < desiredTotal:
            return False
        self.memo = {}
        nums = range(1, maxChoosableInteger + 1)
        return self.helper(nums, desiredTotal)

    def helper(self, nums, desiredTotal):

        key = str(nums)
        if key in self.memo:
            return self.memo[key]

        # means this player can choose at least one number to get a win
        if nums[-1] >= desiredTotal:
            return True

        # the length of nums could change
        for i in xrange(len(nums)):
            # instead of using a used list to past around, build a completly
            #   new list in every loop so we don't need to put back the used num
            #   after each loop, so that we could avoid error
            if not self.helper(nums[:i] + nums[i + 1:], desiredTotal - nums[i]):
                self.memo[key] = True
                return True

        self.memo[key] = False
        return False



Sol = Solution()
print Sol.canIWin(11, 43)



'''
# python application without global variable but using same idea with:
#   https://discuss.leetcode.com/topic/68896/java-solution-using-hashmap-with-detailed-explanation/2
# somehow got TLE because this fucking stupid leetcode

class Solution(object):
    def canIWin(self, maxChoosableInteger, desiredTotal):

        if (1 + maxChoosableInteger) * maxChoosableInteger / 2 < desiredTotal:
            return False
        if desiredTotal <= 0: return True

        self.memo = {}
        used = [0 for i in xrange(maxChoosableInteger + 1)]
        return self.helper(used, desiredTotal)

    def helper(self, used, desiredTotal):

        key = str(used)
        if key in self.memo:
            return self.memo[key]
        if desiredTotal < 1:
            return False

        for i in xrange(1, len(used)):
            if used[i]: continue
            used[i] = 1
            if not self.helper(used, desiredTotal - i):
                self.memo[key] = True
                used[i] = 0
                return True
            used[i] = 0

        self.memo[key] = False
        return False
'''


