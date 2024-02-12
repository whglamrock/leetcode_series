from collections import defaultdict
from typing import List

class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        groupSizeToPeople = defaultdict(set)
        for i, size in enumerate(groupSizes):
            groupSizeToPeople[size].add(i)

        sizeToGroups = defaultdict(list)
        groups = []

        for i, size in enumerate(groupSizes):
            sizeToGroups[size].append(i)
            if len(sizeToGroups[size]) == size:
                groups.append(sizeToGroups[size])
                del sizeToGroups[size]

        return groups
