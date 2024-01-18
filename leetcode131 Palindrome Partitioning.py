from typing import List

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ans = []
        self.dfs(s, [], ans)
        return ans

    def dfs(self, s: str, curr: List[str], ans: List[List[str]]):
        if not s:
            ans.append(curr)
            return

        for i in range(1, len(s) + 1):
            if self.isPalindrome(s[:i]):
                self.dfs(s[i:], curr + [s[:i]], ans)
        return ans

    def isPalindrome(self, s: str) -> bool:
        n = len(s)
        for i in range(n // 2):
            if s[i] != s[n - 1 - i]:
                return False
        return True


print(Solution().partition("ccaacabacb"))
