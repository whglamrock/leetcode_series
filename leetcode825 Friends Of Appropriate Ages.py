from collections import Counter
from typing import List

# 0.5 * x + 7 < y <= x. Below solution is O(n) because 1 <= ages[i] <= 120.
# We can also use binary search solution after sorting the ages
class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        ageCount = Counter(ages)
        numOfReqs = 0
        for age in ages:
            minAge = age // 2 + 8
            for friendAge in range(minAge, age + 1):
                if friendAge not in ageCount:
                    continue
                numOfReqs += ageCount[friendAge]
                if friendAge == age:
                    numOfReqs -= 1

        return numOfReqs
