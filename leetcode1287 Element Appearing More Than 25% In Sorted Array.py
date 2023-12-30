from typing import List

class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        n = len(arr)
        numOfSameNumbers = 0
        target = n / 4
        for i, num in enumerate(arr):
            if i > 0 and num == arr[i - 1]:
                numOfSameNumbers += 1
            else:
                numOfSameNumbers = 1
            # print(numOfSameNumbers, target)
            if numOfSameNumbers > target:
                return num

        return -1


print(Solution().findSpecialInteger(arr=[1, 2, 2, 6, 6, 6, 6, 7, 10]))
print(Solution().findSpecialInteger(arr=[1, 1]))
print(Solution().findSpecialInteger(arr=[1, 2, 3, 3]))
