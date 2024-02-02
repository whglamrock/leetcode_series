from collections import defaultdict
from typing import List

class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        minNum, maxNum = min(nums), max(nums)
        if minNum == maxNum:
            return 0

        buckets = defaultdict(set)
        bucketSize = max((maxNum - minNum) // len(nums), 1)
        for num in nums:
            bucketIndex = (num - minNum) // bucketSize
            buckets[bucketIndex].add(num)

        maxGap = 0
        prevBucketIndex = None
        for i in range((maxNum - minNum) // bucketSize + 1):
            if i not in buckets:
                continue
            if len(buckets[i]) == 2:
                maxGap = max(max(buckets[i]) - min(buckets[i]), maxGap)
            if prevBucketIndex is not None:
                maxGap = max(min(buckets[i]) - max(buckets[prevBucketIndex]), maxGap)
            prevBucketIndex = i

        return maxGap
