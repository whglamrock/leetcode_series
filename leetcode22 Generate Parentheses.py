from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        self.dfs(n, n, '', ans)
        return ans

    def dfs(self, left: int, right: int, curr: str, ans: List[str]):
        if right == left == 0:
            ans.append(curr)
            return
        if left > 0:
            self.dfs(left - 1, right, curr + '(', ans)
        # we need to make sure right is always >= left. otherwise it's invalid
        if right > left:
            self.dfs(left, right - 1, curr + ')', ans)


print(Solution().generateParenthesis(4))
print(Solution().generateParenthesis(7))
