class Solution(object):
    def generateParenthesis(self, n):
        if not n:
            return []
        left, right, ans = n, n, []
        self.dfs(left,right, ans, "")
        return ans

    def dfs(self, left, right, ans, string):
        if left==right==0:
            ans.append(string)
            #return (this return can be saved)
        if left:
            self.dfs(left-1, right, ans, string + "(")
        if right and right>left:
            self.dfs(left, right-1, ans, string + ")")

n = 4
Sol = Solution()
print Sol.generateParenthesis(n)




