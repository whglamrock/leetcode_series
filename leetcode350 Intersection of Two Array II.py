
from collections import Counter

class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        ans = []
        numCount1 = Counter(nums1)
        numCount2 = Counter(nums2)

        for num in numCount1:
            if num not in numCount2:
                continue
            count1, count2 = numCount1[num], numCount2[num]
            for i in xrange(min(count1, count2)):
                ans.append(num)

        return ans



print Solution().intersect([1, 2, 2, 1], [2, 3, 2])
