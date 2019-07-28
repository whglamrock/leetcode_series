
import random

# python's random.randrange() excludes the upper bound but includes the lower bound

class Solution(object):
    def __init__(self, w):
        """
        :type w: List[int]
        """
        self.current = 0
        self.accumToIndex = {}
        self.accum = []
        for i, num in enumerate(w):
            self.current += num
            self.accum.append(self.current)
            self.accumToIndex[self.current] = i

    # binary search to find the first number >= the randomNum
    def pickIndex(self):
        """
        :rtype: int
        """
        randomNum = random.randint(1, self.current)
        l, r = 0, len(self.accum) - 1

        # bear in mind that the exit creterion is l == r
        while l < r:
            m = (l + r) / 2
            if self.accum[m] == randomNum:
                return self.accumToIndex[self.accum[m]]
            # m is not candidate; when l == m this condition is impossinle
            elif self.accum[m] < randomNum:
                l = m + 1
            # m is still candidate
            else:
                r = m

        return self.accumToIndex[self.accum[l]]



# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()