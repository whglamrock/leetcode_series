
# recursive solution

class Solution(object):
    def subsets(self, nums):

        if (not nums):
            return [[]]

        ans = []    # no need to sort, because all numbers in nums are distinct
        def dfs(lastindex, already):
            ans.append(already)
            if lastindex == len(nums) - 1:
                return

            for i in xrange(lastindex + 1, len(nums)):
                dfs(i, already + [nums[i]])

        dfs(-1, [])
        return ans



nums = [1,2,3,4]
Sol = Solution()
ans = Sol.subsets(nums)
print ans



'''
# iterative solution
class Solution(object):
    def subsets(self, nums):

        ans = []    # no need to sort
        pre = []
        while (not pre) or len(pre[-1]) <= len(nums):
            if (not pre):
                for i in xrange(len(nums)):
                    pre.append([nums[i],i])
                    ans.append([nums[i]])
            else:
                next = []
                for item in pre:
                    index = item.pop()
                    for j in xrange(index+1, len(nums)):
                        next.append(item+[nums[j],j])
                        ans.append(item+[nums[j]])
                pre = next
        ans.append([])

        return ans
'''