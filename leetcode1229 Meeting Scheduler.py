from typing import List

class Solution:
    def minAvailableDuration(self, slots1: List[List[int]], slots2: List[List[int]], duration: int) -> List[int]:
        slots1.sort()
        slots2.sort()
        i, j = 0, 0
        m, n = len(slots1), len(slots2)
        while i < m and j < n:
            overlapping = self.findOverlapping(slots1[i], slots2[j])
            if overlapping[1] - overlapping[0] >= duration:
                return [overlapping[0], overlapping[0] + duration]
            else:
                if slots1[i][1] <= slots2[j][1]:
                    i += 1
                else:
                    j += 1

        return []

    def findOverlapping(self, slot1: List[int], slot2: List[int]) -> List[int]:
        if slot1[1] <= slot2[0]:
            return [-1, -1]
        if slot2[1] <= slot1[0]:
            return [-1, -1]

        return [max(slot1[0], slot2[0]), min(slot1[1], slot2[1])]
