'''
O(n) time complexity; O(1) space complexity algorithm. This algorithm only works when majority exists.
'''
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        for i in range(len(nums)):
            if count == 0:     # when count hits 0, it means the total amount of all other different
                majority = nums[i] # "elements" is same as the one of the previously dumped "majority"
                count += 1 # So the "majority" needs to change
                continue
# After the majority changes, it is actually implementing the code in the rest of of "nums" list;
# The previous part is "dumped"
            if majority != nums[i]: # at this moment, though the count-=1, the majority
                count -= 1          # still remains same until count hits 0.
            else:
                count += 1

        return majority


Sol = Solution()
a = [1,2,2,1,2,1,2,1]
print Sol.majorityElement(a)



