from typing import List

class Solution:
    def arraysIntersection(self, arr1: List[int], arr2: List[int], arr3: List[int]) -> List[int]:
        i, j, k = 0, 0, 0
        ans = []
        while i < len(arr1) and j < len(arr2) and k < len(arr3):
            if arr1[i] == arr2[j] == arr3[k]:
                ans.append(arr1[i])
                i += 1
                j += 1
                k += 1
            else:
                maxOf3 = max(arr1[i], arr2[j], arr3[k])
                if arr1[i] != maxOf3:
                    i += 1
                if arr2[j] != maxOf3:
                    j += 1
                if arr3[k] != maxOf3:
                    k += 1

        return ans
