class Solution(object):
    def wiggleSort(self, nums):

        i = 0
        while i < len(nums)-1:
            if i%2 == 0:
                if nums[i+1] < nums[i]:
                    temp = nums[i+1]
                    nums[i+1] = nums[i]
                    nums[i] = temp
            else:
                if nums[i+1] > nums[i]:
                    temp = nums[i+1]
                    nums[i+1] = nums[i]
                    nums[i] = temp
            i += 1

        #return nums     # the leetcode asks for returning nothing.

Sol = Solution()
nums = [2,9,8,7,2,1,5,6,4]
print Sol.wiggleSort(nums)




