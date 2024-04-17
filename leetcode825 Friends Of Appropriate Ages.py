from collections import Counter, defaultdict
from math import floor
from typing import List


# 0.5 * x + 7 < y <= x; also 0.5 * x + 7 needs to < x
class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        ageCount = Counter(ages)
        ageToNumOfPeopleNotOlder = defaultdict(int)
        for age in range(1, 121):
            ageToNumOfPeopleNotOlder[age] = ageToNumOfPeopleNotOlder[age - 1] + ageCount[age]

        numOfReqs = 0
        for age in ages:
            minAge = floor(age / 2 + 7)
            if minAge >= age:
                continue
            numOfReqs += ageToNumOfPeopleNotOlder[age] - ageToNumOfPeopleNotOlder[minAge] - 1

        return numOfReqs
