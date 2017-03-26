
# if we set the secondmaximum and thirdmaximum to -2147483648 initially,
# we need to worry about the test case like [-2147483648, 1, 2].

class Solution(object):
    def thirdMax(self, nums):

        if len(nums) < 3:
            return max(nums)

        maximum = max(nums)
        secondmaximum = None
        thirdmaximum = None
        i, n = 0, len(nums)
        while i < n:
            if nums[i] < maximum:
                if secondmaximum == None or nums[i] > secondmaximum:
                    secondmaximum = nums[i]
            i += 1
        if secondmaximum == None: return maximum
        i = 0
        while i < n:
            if nums[i] < secondmaximum:
                if thirdmaximum == None or nums[i] > thirdmaximum:
                    thirdmaximum = nums[i]
            i += 1

        if thirdmaximum != None:
            return thirdmaximum
        else:
            return maximum
