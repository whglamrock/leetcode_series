# bitwise manipulate trick
# '&': binary AND (for a=0101, b=0100, a&b=0100), if the digit of both numbers is 1, it comes out 1; otherwise 0
class Solution(object):
    def intersection(self, nums1, nums2):

        # '&' means the intersection of two sets
        return list(set(nums1) & set(nums2))