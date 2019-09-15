
# when encountering this question in the real interview, need to ask whether something like [0, 1, 2, 3, 4, 5]
    # is possible

class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #no need to consider the empty case because it doesn't make any sense for minimum

        l, r = 0, len(nums) - 1
        while l <= r:
            m = l + (r - l) / 2
            if nums[l] <= nums[m] <= nums[r]:
                return nums[l]
            # nums[l] == nums[m] is when search range only contains 1 or 2 nums
            # in fact in real interviews, we may find ourselves diving the following
              # elif condition into 2: 1) nums[l] == nums[m]; 2) nums[l] < nums[m]
            elif nums[l] <= nums[m]:
                l = m + 1
            # in this case, m is still candidate index
            else:
                # the only time r == m causes infinite loop is when search range is 1,
                    # which ic covered by first if condition
                r = m



Sol = Solution()
nums = [4,5,6,7,0,1,2]
print Sol.findMin(nums)
