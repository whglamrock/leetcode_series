from typing import List

# The idea is: if car starts at A and can not reach B. Any station between A and B can not reach B.
# i.e., we need move the potential start station to B + 1
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1

        tank = 0
        start = 0
        for i in range(len(gas)):
            tank += gas[i] - cost[i]
            if tank < 0:
                tank = 0
                start = i + 1

        return start


print(Solution().canCompleteCircuit([2, 5, 1, 8, 4, 5, 2], [1, 1, 8, 2, 7, 3, 4]))
print(Solution().canCompleteCircuit([5, 8, 2, 8], [6, 5, 6, 6]))
