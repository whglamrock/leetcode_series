
# see explanation from: https://discuss.leetcode.com/topic/79923/c-16ms-o-n-solution-with-trivial-proof/2
# the key idea: use each machines[i] as a pivot and check if both sides are balanced; then if
#   it happens for every machines[i], every machines[i] will be at the desired average value

class Solution(object):
    def findMinMoves(self, machines):

        if not machines:
            return 0

        n = len(machines)
        sumarray = [0 for i in xrange(n + 1)]
        for i in xrange(n):
            sumarray[i + 1] = sumarray[i] + machines[i]

        if sumarray[-1] % n != 0:
            return -1

        avg = sumarray[-1] / n
        res = 0

        # after each for loop, we keep balance for two sides of each machines[i]
        #   -- it means the sum in both sides meets requirements
        #   but not necessarily every machines gets to the desired average value
        for i in xrange(n):
            l = i * avg - sumarray[i]
            # it is n - i - 1, not n - i. Cuz you needa rule out machines[i] itself
            r = (n - i - 1) * avg - (sumarray[-1] - sumarray[i] - machines[i])  # or sumarray[-1] - sumarray[i + 1]
            if l > 0 and r > 0:
                res = max(res, l + r)
            else:
                res = max(res, max(abs(l), abs(r)))

        return res



machines = [1, 0, 5]
Sol = Solution()
print Sol.findMinMoves(machines)
