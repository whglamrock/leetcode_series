
from collections import deque

class Solution(object):
    def shortestToChar(self, S, C):
        """
        :type S: str
        :type C: str
        :rtype: List[int]
        """
        dq = deque()
        ans = []
        prevIndex = None

        for i, char in enumerate(S):
            if char == C:
                while dq:
                    j = dq.popleft()
                    if prevIndex != None:
                        ans.append(min(j - prevIndex, i - j))
                    else:
                        ans.append(i - j)
                ans.append(0)
                prevIndex = i
            else:
                dq.append(i)

        while dq:
            ans.append(dq.popleft() - prevIndex)

        return ans



Sol = Solution()
print Sol.shortestToChar(S = "loveleetcode", C = 'e')