
# in the while loop if we use "while j < n and nums[j] == 0: j += 1" to find the first non-zero number,
    # we need to REMEMBER to check if j still < n before we do the swap

class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        if not nums:
            return

        count = 0
        for num in nums:
            if num == 0:
                count += 1

        i, j = 0, 0
        n = len(nums)
        while j < n:
            # using if this way instead of while loop to identify a non-zero number,
                # so we can avoid checking if j still < n after the while loop
            if nums[j] != 0:
                nums[i] = nums[j]
                i += 1
            j += 1

        k = n - 1
        while count:
            nums[k] = 0
            count -= 1
            k -= 1



nums = [0, 1, 0, 3, 12]
Solution().moveZeroes(nums)
print nums



'''
# without counting the number of zeros

class Solution(object):
    def moveZeroes(self, nums):
    
        if not nums:
            return
                        
        i, j = 0, 0
        n = len(nums)
        while i < n and j < n:
            # j find the first non-zero number
            while j < n and nums[j] == 0:
                j += 1
            if j >= n:
                break
            tmp = nums[i]
            nums[i] = nums[j]
            nums[j] = tmp
            i += 1
            j += 1
'''