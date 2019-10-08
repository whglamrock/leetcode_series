
class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        if n == 0:
            return []

        ans = []
        self.dfs(n, n, ans, '')
        return ans

    def dfs(self, left, right, ans, curr):
        if left == 0 and right == 0:
            ans.append(curr)
            return
        if left:
            self.dfs(left - 1, right, ans, curr + '(')
        if right > left:
            self.dfs(left, right - 1, ans, curr + ')')



print Solution().generateParenthesis(4)
print Solution().generateParenthesis(3)




