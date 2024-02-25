from collections import defaultdict
from typing import List

# Idea came from: https://leetcode.com/problems/minimum-total-cost-to-make-arrays-unequal/solutions/2897969/c-simple-greedy-in-o-n-with-explanation/
# 1) For all equal indexes, there is no way you can not swap any of them. If there is no dominant number (any nums1[i]
# that appears more than half of equal indexes) we can simply return sum(EqualIndexes)
# 2) In case where there is a dominant number, we need to incorporate some unequalIndexes and each
# nums1/2[unequalIndex] != dominant number. You can counter prove that if you include any nums1/2[unequalIndex] == dominant number
# things will get worse:
# 2.1) Assume the number of extra dominant numbers is x (i.e. num of dominant numbers - x == num of non dominant numbers);
# 2.2) For each x dominant number you will need to find an extra unequalIndex in nums1 to deal with it.
# If nums1[unequalIndex] == dominant number or nums2[unequalIndex] == dominant number the swap will become meaningless.
class Solution:
    def minimumTotalCost(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        equalNumCount = defaultdict(int)
        totalNumOfEquals = 0
        equalIndexes = set()
        for i in range(n):
            if nums1[i] != nums2[i]:
                continue
            equalNumCount[nums1[i]] += 1
            totalNumOfEquals += 1
            equalIndexes.add(i)
        if not equalNumCount:
            return 0

        dominantCount = max(equalNumCount.values())
        if dominantCount <= totalNumOfEquals // 2:
            return sum(equalIndexes)

        dominantNum = None
        for num in equalNumCount:
            if equalNumCount[num] == dominantCount:
                dominantNum = num
                break

        numOfIndexesToAdd = 2 * dominantCount - len(equalIndexes)
        for i in range(n):
            if i in equalIndexes or nums1[i] == dominantNum or nums2[i] == dominantNum:
                continue
            equalIndexes.add(i)
            numOfIndexesToAdd -= 1
            if not numOfIndexesToAdd:
                return sum(equalIndexes)

        return -1
