from typing import List

# see: https://leetcode.com/problems/last-moment-before-all-ants-fall-out-of-a-plank/solutions/720189/java-c-python-ants-keep-walking-o-n/
# when two ants A and B meet and change direction, it's same as they don't change direction and keep walking,
# with A and B swapped.
class Solution:
    def getLastMoment(self, n: int, left: List[int], right: List[int]) -> int:
        ans = 0
        for i in left:
            ans = max(ans, i)
        for j in right:
            ans = max(ans, n - j)
        return ans


print(Solution().getLastMoment(n=4, left=[4, 3], right=[0, 1]))
print(Solution().getLastMoment(n=7, left=[], right=[0, 1, 2, 3, 4, 5, 6, 7]))
