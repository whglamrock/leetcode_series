
# For O(n) space solution we can keep an current min from left to right and current max from right to left,
    # then check if min(nums[:i]) < nums[i] < max(nums[i + 1:])

# If in interview there is a specific requirement for O(1) space requirement, this becomes a > medium but
    # slightly < hard question
# The basic idea is:
    # 1) For an increasing triplet, the must exist 2 numbers that < the current nums[i]
    # 2) Between the previous 2 numbers, the smaller one must appear before the bigger one
    # 3) the "elif" condition makes sure that 2) will always be satisfied when we found a candidate nums[i]
    # 4) try special test cases like: [4, 5, 1, 5]; [4, 5, 1, 2, 3]

class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if not nums or len(nums) < 3:
            return False

        smallest, secondSmallest = 2147483647, 2147483647
        for num in nums:
            if num > smallest and num > secondSmallest:
                return True
            # not "<"  because we need to deal with duplicates. e.g., [1, 1, 1, 1, 1], [1, 1, -2, 6]
            # since don't allow smallest == secondSmallest, when we found duplicates we must update smallest
            elif num <= smallest:
                smallest = num
            # smallest < num <= secondSmallest
            else:
                secondSmallest = num

        return False



print Solution().increasingTriplet([9, 4, 3, 1, 6, 2, 8])
print Solution().increasingTriplet([1, 1, 1, 1])



'''
O(n) space solution. Should also work in real interview
class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if not nums or len(nums) < 3:
            return False
        
        n = len(nums)
        currentMins = [0] * n
        currentMaxs = [0] * n
        currentMin, currentMax = 2147483647, -2147483648
        
        for i, num in enumerate(nums):
            currentMin = min(currentMin, num)
            currentMins[i] = currentMin
        
        for i in xrange(n - 1, -1, -1):
            num = nums[i]
            currentMax = max(currentMax, num)
            currentMaxs[i] = currentMax
        
        for i in xrange(1, n - 1):
            if nums[i] > currentMins[i - 1] and nums[i] < currentMaxs[i + 1]:
                return True
        
        return False
'''