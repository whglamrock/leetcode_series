from collections import deque
from typing import List


# This is a fairly complicated sliding window question, in the sense that the computation of delta when appending/popping
# elements to/from the deque. In real interview, the most tricky part is understand that in some subarray if we have x
# number of certain value, the total pair is actually the num of combination of all indexes: x * (x - 1) // 2.
class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        numOfEqualPairs = 0
        window = {}
        ans = 0
        l = 0
        for r, num in enumerate(nums):
            if num not in window:
                window[num] = deque()
            window[num].append(r)
            newRightNumCount = len(window[num])
            oldRightNumCount = newRightNumCount - 1
            oldNumOfPairsForRightNum = max(0, oldRightNumCount * (oldRightNumCount - 1) // 2)
            newNumOfPairsForRightNum = newRightNumCount * (newRightNumCount - 1) // 2
            addedNumOfPairs = newNumOfPairsForRightNum - oldNumOfPairsForRightNum
            numOfEqualPairs += addedNumOfPairs

            while l <= r and numOfEqualPairs >= k:
                leftNum = nums[l]
                oldLeftNumCount = len(window[leftNum])
                newLeftNumCount = oldLeftNumCount - 1
                oldNumOfPairsForLeftNum = oldLeftNumCount * (oldLeftNumCount - 1) // 2
                newNumOfPairsForLeftNum = max(0, newLeftNumCount * (newLeftNumCount - 1) // 2)
                reducedNumOfPairs = oldNumOfPairsForLeftNum - newNumOfPairsForLeftNum

                if numOfEqualPairs - reducedNumOfPairs < k:
                    break
                window[leftNum].popleft()
                numOfEqualPairs -= reducedNumOfPairs
                if not window[leftNum]:
                    del window[leftNum]
                l += 1

            if numOfEqualPairs >= k:
                ans += l + 1

        return ans
