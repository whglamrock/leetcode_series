
# If car starts at A and can not reach B. Any station between A and B can not reach B. i.e.,
    # B is the first station that A can not reach.
# If the total number of gas is bigger than the total number of cost. There must be a solution.

class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        if sum(gas) < sum(cost):
            return -1

        n = len(gas)
        start = 0
        tank = 0

        for i in xrange(n):
            tank += gas[i] - cost[i]
            # If tank < 0, it means the original start A cannot reach B;
            # Then any point between A and B cannot reach B
            if tank < 0:
                tank = 0
                start = i + 1

        return start



print Solution().canCompleteCircuit([2, 5, 1, 8, 4, 5, 2], [1, 1, 8, 2, 7, 3, 4])

