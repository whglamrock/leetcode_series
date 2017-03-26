
# O(N) time solution.

class Solution(object):
    def summaryRanges(self, nums):

        if (not nums):
            return []

        ans = []
        start, end = nums[0], nums[0]

        i = 0
        while i < len(nums):    # the exit condition will overlook the last pair
            if i < len(nums) - 1 and nums[i] + 1 != nums[i + 1]:
                end = nums[i]
                if start != end:
                    ans.append(str(start) + '->' + str(end))
                else:
                    ans.append(str(start))
                start, end = nums[i + 1], nums[i + 1]
            i += 1

        # add the last pair.
        end = nums[-1]
        if start != end:
            ans.append(str(start) + '->' + str(end))
        else:
            ans.append(str(start))

        return ans



Sol = Solution()
nums = [0, 1, 2, 4, 5, 7, 9, 11, 13]
print Sol.summaryRanges(nums)
