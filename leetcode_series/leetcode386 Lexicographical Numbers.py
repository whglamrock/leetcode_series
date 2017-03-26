
# my original, which happens to the most elegant, solution.
# O(n) time, O(1) space.

class Solution(object):
    def lexicalOrder(self, n):

        ans = [1]
        while len(ans) < n:
            new = ans[-1] * 10
            while new > n:
                new /= 10
                new += 1
                while new % 10 == 0:    # deal with case like 199+1=200 when we need to restart from 2.
                    new /= 10
            ans.append(new)

        return ans



Sol = Solution()
print Sol.lexicalOrder(500)