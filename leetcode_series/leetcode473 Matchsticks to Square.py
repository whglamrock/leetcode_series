
# a very classic DFS question. remember the DFS idea

class Solution(object):
    def makesquare(self, nums):

        if not nums or len(nums) < 4: return False
        sumnums = sum(nums)
        if sumnums % 4 != 0: return False

        nums.sort()
        nums.reverse()

        # the parameter sums store the sum value of four subsets, respectively
        def dfs(nums, sums, index, target):

            if index == len(nums):
                if sums[0] == target and sums[1] == target and sums[2] == target:
                    return True
                return False

            for i in xrange(4):
                if sums[i] + nums[index] > target:
                    continue
                sums[i] += nums[index]
                if dfs(nums, sums, index + 1, target):
                    return True
                sums[i] -= nums[index]

            return False

        return dfs(nums,[0, 0, 0, 0], 0, sumnums / 4)