
# Iterative Solution:

class Solution(object):
    def permute(self, nums):
        perms = [[]]
        for n in nums:
            new_perms = []
            for perm in perms:
                for i in range(len(perm)+1):
                    new_perms.append(perm[:i] + [n] + perm[i:])   ###insert n
            perms = new_perms #every perms is based on the last-level perms(e.g. if last-level
            # perm = [[2,1],[1,2]], the first three list elements in perm are [3,2,1],[2,3,1],[2,1,3],
            # which come from inserting "3" to different spots in [2,1]; the 2nd of last three elements
            # in perm are [3,1,2],[1,3,2],[1,2,3], based on [1,2] from last-level perm)

        return perms



'''
# recursive solution:

class Solution(object):
    def permute(self, nums):
        res = []
        self.dfs(nums, [], res)
        return res

    def dfs(self, nums, path, res):
        if not nums:
            res.append(path)
            # return # backtracking
        for i in xrange(len(nums)):
            self.dfs(nums[:i]+nums[i+1:], path+[nums[i]], res)
'''
