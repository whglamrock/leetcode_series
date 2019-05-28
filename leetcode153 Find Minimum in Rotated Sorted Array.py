
class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return -1

        l, r = 0, len(nums) - 1
        while l <= r:
            m = (l + r) / 2
            if nums[l] <= nums[m] <= nums[r]:
                return nums[l]
            # nums[l] == nums[m] is when search range only contains 1 or 2 nums
            # in fact in real interviews, we may find ourselves diving the following
              # elif condition into 2: 1) nums[l] == nums[m]; 2) nums[l] < nums[m]
            elif nums[l] <= nums[m]:
                l = m + 1
            # in this case, m is still candidate index
            else:
                # consider when in next loop the search range becomes 1, the first if condition will satisfy
                r = m



Sol = Solution()
nums = [4,5,6,7,0,1,2]
print Sol.findMin(nums)
