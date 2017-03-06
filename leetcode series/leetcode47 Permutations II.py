# no extra space.
class Solution(object):
    def permuteUnique(self, nums):

        ans = [[]]
        for n in nums:
            new_ans = []
            for l in ans:
                for i in xrange(len(l)+1):
                    new_ans.append(l[:i]+[n]+l[i:])
                    if i < len(l) and l[i] == n: break    #handles duplication
            ans = new_ans

        return ans


Sol = Solution()
nums = [1,2,3]
print Sol.permuteUnique(nums)

'''
# my original not clean code with o(n^2) space.
import copy
class Solution(object):
    def permuteUnique(self, nums):

        dick = {}
        for num in nums:
            if num not in dick:
                dick[num] = 1
            else:
                dick[num] += 1

        todo = [([], dick)]
        ans = []
        while todo:
            prev, newdick = todo.pop()
            if (not newdick):
                ans.append(prev)
            for item in newdick:
                next = prev + [item]
                nextdick = copy.copy(newdick)
                nextdick[item] -= 1
                if nextdick[item] == 0:
                    del nextdick[item]
                todo.append((next, nextdick))

        return ans
'''
