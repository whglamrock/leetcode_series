
# Remember the different between pre = costs[0][:] and pre = costs[0]. The use of '[:]' is essential

class Solution(object):
    def minCost(self, costs):
        size = len(costs)
        if size == 0:
            return 0

        pre = costs[0][:]
        now = [0]*3

        for i in xrange(size-1):    # This iterative solution is actually doable.
            now[0] = min(pre[1], pre[2]) + costs[i+1][0] # 'now' always represents currently optimal solution
            now[1] = min(pre[0], pre[2]) + costs[i+1][1]
            now[2] = min(pre[0], pre[1]) + costs[i+1][2]
            pre[:] = now[:]

        return pre



costs = [[1,2,3],[3,1,6],[32,6,11],[1,71,23],[4,6,3]]
Sol = Solution()
print Sol.minCost(costs)

