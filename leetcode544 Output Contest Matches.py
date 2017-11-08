
from collections import deque

# O(nlogn) solution

class Solution(object):
    def findContestMatch(self, n):

        ans = [str(i) for i in xrange(1, n + 1)]
        ans = deque(ans)

        while len(ans) > 1:
            newans = deque()
            while ans:
                newpair = '(' + ans.popleft() + ',' + ans.pop() + ')'
                newans.append(newpair)
            ans = newans

        return ans[0]



Sol = Solution()
print Sol.findContestMatch(16)
