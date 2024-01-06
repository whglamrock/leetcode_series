from heapq import *
from typing import List

# idea similar to leetcode 1353: use a priorityQueue to store all open flowers (storing the closing times)
# sort the people by arrivalTime, add the open flowers to the queue then pop out the closed flowers
class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:
        arrivalTimeWithPeopleIndex = []
        for i, arrivalTime in enumerate(people):
            arrivalTimeWithPeopleIndex.append([arrivalTime, i])
        arrivalTimeWithPeopleIndex.sort()
        # sort by opening time
        flowers.sort()

        ans = [0] * len(people)
        openFlowers = []
        i = 0
        for item in arrivalTimeWithPeopleIndex:
            arrivalTime, peopleIndex = item[0], item[1]
            # need to add the open flowers first because the new
            # arrivalTime can be > some of the unvisited flowers[i][1]
            while i < len(flowers) and flowers[i][0] <= arrivalTime:
                heappush(openFlowers, flowers[i][1])
                i += 1
            # pop out the closed flowers
            while openFlowers and openFlowers[0] < arrivalTime:
                heappop(openFlowers)

            ans[peopleIndex] = len(openFlowers)

        return ans


