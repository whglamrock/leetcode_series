
# If car starts at A and can not reach B. Any station between A and B can not reach B. i.e.,
    # B is the first station that A can not reach.
# If the total number of gas is bigger than the total number of cost. There must be a solution.

class Solution(object):
    def canCompleteCircuit(self, gas, cost):

        # total means how much gas we "owe" so far
        start, total, tank = 0, 0, 0

        n = len(gas)
        for i in xrange(n):
            tank += gas[i] - cost[i]
            if tank < 0:
                start = i + 1
                total += tank
                tank = 0

        return start if total + tank >= 0 else -1



gas = [2, 5, 1, 8, 4, 5, 2]
cost = [1, 1, 8, 2, 7, 3, 4]
print Solution().canCompleteCircuit(gas, cost)

