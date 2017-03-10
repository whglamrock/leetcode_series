class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        while i+1<len(nums):
            if nums[i] == nums[i+1]:
                del nums[i]
            else:
                i += 1

        return len(nums)

a = [1,1,1,1,1,2,2,2,3,4,6,7,9]
objct = Solution()
print objct.removeDuplicates(a)