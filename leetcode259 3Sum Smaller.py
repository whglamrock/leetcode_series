
class Solution(object):
    def threeSumSmaller(self, nums, target):

        nums.sort()
        ans = 0

        for i in xrange(0, len(nums) - 2):
            if 3*nums[i] >= target: # very important for reducing the number of loops
                return ans

            start = i + 1
            end = len(nums) - 1

            while start < end:
                if nums[i] + nums[start] + nums[end] < target:
                    ans += end - start  # for a certain 'start', replace the 'end' with numbers on
                    # the left side of 'end', the if statement still exists.
                    start += 1
                else:
                    end -= 1  # for this 'end', the smallest 'start': nums[i+1] can't work, so we
                    # need to reduce the end.

        return ans



Sol = Solution()
nums = [-2, 0, 1, 3]
target = 2
print Sol.threeSumSmaller(nums,target)




