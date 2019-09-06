
# Greedy algorithm: deal with the tallest people first.
# P.S. remember how python sort lambda is used

class Solution(object):
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        if not people:
            return []
        people.sort(key=lambda x: (-x[0], x[1]))

        ans = []
        for h, k in people:
            ans.insert(k, [h, k])

        return ans



print Solution().reconstructQueue([[7, 0], [4, 4], [7, 1], [5, 0], [6, 1], [5, 2]])

