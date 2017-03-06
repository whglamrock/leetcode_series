# set up two pointers to extend the 'window'.
class Solution(object):
    def canCompleteCircuit(self, gas, cost):

        start = len(gas)-1
        end = 0

        summary = gas[start]-cost[start]
        while end < start:
            if summary >= 0:
                summary += gas[end]-cost[end]
                end += 1
            else:
                start -= 1
                summary += gas[start]-cost[start]

        if summary >= 0:
            return start
        else:
            return -1


gas = [2,5,1,8,4,5,2]
cost = [1,1,8,2,7,3,4]
gasminuscost = []
for i in xrange(len(gas)):
    gasminuscost.append(gas[i]-cost[i])
print gasminuscost
Sol = Solution()
print Sol.canCompleteCircuit(gas, cost)

