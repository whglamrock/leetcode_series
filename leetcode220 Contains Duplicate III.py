from typing import List

class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], indexDiff: int, valueDiff: int) -> bool:
        bucket = {}
        for i, num in enumerate(nums):
            if valueDiff != 0:
                bucketIndex = num // valueDiff
                leftIndex, rightIndex = bucketIndex - 1, bucketIndex + 1
            else:
                bucketIndex = num
                leftIndex, rightIndex = bucketIndex, bucketIndex

            # e.g., when num = 1 and valueDiff = 3, and 4 is in bucket[1], we need to not only check
            # bucket[index] but also its left & right bucket
            for j in range(leftIndex, rightIndex + 1):
                if j in bucket and abs(bucket[j] - num) <= valueDiff:
                    return True

            # 1) there are at most indexDiff buckets and each bucket stores only 1 number
            # 2) we only care about the i - 1, i - 2, ...i - indexDiff 's corresponding buckets, no matter
            # whether these buckets fall into the [leftIndex, rightIndex + 1] range
            bucket[bucketIndex] = num
            if len(bucket) > indexDiff:
                if valueDiff != 0:
                    del bucket[nums[i - indexDiff] // valueDiff]
                else:
                    del bucket[nums[i - indexDiff]]

        return False
