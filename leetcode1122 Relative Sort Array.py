from collections import Counter
from typing import List


class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        ans = []
        counter1 = Counter(arr1)
        for num in arr2:
            if num in counter1:
                for i in range(counter1[num]):
                    ans.append(num)

        arr2Nums = set(arr2)
        numsNotInArr2 = []
        for num in arr1:
            if num not in arr2Nums:
                numsNotInArr2.append(num)
        numsNotInArr2.sort()

        return ans + numsNotInArr2
