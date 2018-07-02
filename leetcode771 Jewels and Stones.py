
# a meaningless question

class Solution(object):
    def numJewelsInStones(self, J, S):

        jewels = set(J)
        count = 0
        for c in S:
            if c in jewels:
                count += 1

        return count