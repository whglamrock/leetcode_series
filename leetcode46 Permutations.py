
# Iterative backtracking

class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return []

        curr = [[]]
        for num in nums:
            next = []
            for permutation in curr:
                for i in xrange(len(permutation) + 1):
                    next.append(permutation[:i] + [num] + permutation[i:])
            curr = next

        return curr



print Solution().permute([1, 2, 3])



'''
# recursive DFS

class Solution(object):
    def permute(self, nums):
        res = []
        self.dfs(nums, [], res)
        return res

    def dfs(self, nums, path, res):
        if not nums:
            res.append(path)
            return
        for i in xrange(len(nums)):
            self.dfs(nums[:i] + nums[i + 1:], path + [nums[i]], res)
'''
