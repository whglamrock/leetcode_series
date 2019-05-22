
# the idea is greedy algorithm

class Solution(object):
    def jump(self, nums):

        # in real interview we need to ask what to return for the corner cases
        if not nums or len(nums) == 1:
            return 0

        start, end = 0, 0
        steps = 0
        n = len(nums)
        farthest = 0

        # within each round of scan, the range is [start, end], inclusive
        # since we don't care about nums[-1], the ceiling for i is n - 2
        while end < n - 1:
            steps += 1

            # core idea of greedy: if we can reach an index with 1 step, we
            # do not use 2. However, each [start, end] range does not necessarily
            # have 1 step index in it
            for i in xrange(start, end + 1):
                farthest = max(farthest, i + nums[i])
            if farthest >= n - 1:
                return steps
            start, end = end + 1, farthest

            # not needed because we assume we will always be able to reach it
            # if start > end:
            #     break

            # not needed because we assume we will always be able to reach it
            # return 2147483647



Sol = Solution()
nums = [2,3,1,1,4]
print Sol.jump(nums)
