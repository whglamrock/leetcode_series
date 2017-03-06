# idea from: https://discuss.leetcode.com/topic/6186/java-backtracking-solution
# notice how this fucker write the backtracking. Always think efficiently using less space for bktrck.
class Solution(object):
    def partition(self, s):

        def check(string):
            i, j = 0, len(string)-1
            while i <= j:
                if string[i] != string[j]:
                    return False
                else:
                    i += 1
                    j -= 1
            return True

        self.ans = []
        def helper(i, cur):
            if i == len(s):
                self.ans.append(cur)
            for j in xrange(i+1, len(s)+1):
                if check(s[i:j]) == True:
                    helper(j, cur+[s[i:j]])

        helper(0, [])
        return self.ans


Sol = Solution()
s = "ccaacabacb"
print Sol.partition(s)
