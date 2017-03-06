# the key is to visualize three conditions when crosses/meets happen.
# idea from: https://discuss.leetcode.com/topic/38014/java-oms-with-explanation/2
class Solution(object):
    def isSelfCrossing(self, x):

        if len(x) <= 3:
            return False

        for i in xrange(3, len(x)):
            if x[i] >= x[i - 2] and x[i - 1] <= x[i - 3]:   # fourth crosses the first and so on
                return True
            if i >= 4:  # fifth meets the first and so on
                if x[i - 1] == x[i - 3] and x[i] + x[i - 4] >= x[i - 2]:
                    return True
            if i >= 5:  # sixth crosses the first and so on
                if x[i - 2] >= x[i - 4] and x[i - 1] <= x[i - 3] and \
                    x[i] + x[i - 4] >= x[i - 2] and x[i - 1] + x[i - 5] >= x[i - 3]:
                    return True

        return False

Sol = Solution()
x = [4,4,10,4,6]
print Sol.isSelfCrossing(x)
