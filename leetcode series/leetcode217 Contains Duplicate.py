class Solution(object):
    def containsDuplicate(self, nums):

        return len(nums) != len(set(nums))

a = [1,2,3,4,5]
Sol = Solution()
print Sol.containsDuplicate(a)


'''
class Solution(object):
    def containsDuplicate(self, nums):

        if (not nums) or len(nums) == 1:
            return False

        nums.sort()
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                return True

        return False
'''



