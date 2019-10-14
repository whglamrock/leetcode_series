
# elegant iterative solution, perfectly using the backtracking idea
# sorting is easier for us to avoid deduping, also it doesn't increase time complexity

class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return [[]]

        ans = [[]]
        nums.sort()

        for num in nums:
            newSubsets = []
            for item in ans:
                newSubsets.append(item + [num])
            ans += newSubsets

        return ans



print Solution().subsets([1, 2, 3, 4])



'''
# classic recursive DFS solution

class Solution(object):
    def subsets(self, nums):

        if not nums:
            return []

        nums.sort()
        self.nums = nums
        self.res = []
        self.dfs(0, [])

        return self.res

    def dfs(self, i, path):

        self.res.append(path)
        for j in xrange(i, len(self.nums)):
            self.dfs(j + 1, path + [self.nums[j]])
'''