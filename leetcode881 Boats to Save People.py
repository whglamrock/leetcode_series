from typing import List

# Binary search solution can also achieve O(N * log(N)) and it's definitely acceptable in real interview (see at the bottom).
# But here, a 2 pointer solution is simpler and runs faster.
class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        i, j = 0, len(people) - 1
        boats = 0
        while i <= j:
            if i < j and people[i] + people[j] <= limit:
                i += 1
                j -= 1
            else:
                j -= 1
            boats += 1

        return boats


'''
class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        visitedIndexes = set()
        r = len(people) - 1
        for i, weight in enumerate(people):
            if r <= i or limit == weight:
                break
            target = limit - weight
            maxIndexCanShareBoat = self.findMaxIndexLessOrEqualThan(people, target, i + 1, r)
            if maxIndexCanShareBoat == -1:
                break
            visitedIndexes.add(i)
            visitedIndexes.add(maxIndexCanShareBoat)
            r = maxIndexCanShareBoat - 1

        return len(visitedIndexes) // 2 + len(people) - len(visitedIndexes)

    def findMaxIndexLessOrEqualThan(self, nums: List[int], target: int, l: int, r: int) -> int:
        while l <= r:
            m = (l + r + 1) // 2
            if l == r:
                if nums[m] <= target:
                    return m
                else:
                    return -1
            if nums[m] <= target:
                l = m
            else:
                r = m - 1

        return -1
'''