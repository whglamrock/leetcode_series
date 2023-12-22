from collections import defaultdict


class Solution(object):
    def minTransfers(self, transactions):
        """
        :type transactions: List[List[int]]
        :rtype: int
        """
        if not transactions:
            return 0

        netBalance = defaultdict(int)
        for x, y, z in transactions:
            netBalance[x] -= z
            netBalance[y] += z

        debts = []
        for debt in netBalance.values():
            if debt != 0:
                debts.append(debt)

        return self.dfs(debts, 0, 0)

    # backtracking
    def dfs(self, debts, i, numTrans):
        while i < len(debts) and debts[i] == 0:
            i += 1
        if i >= len(debts) - 1:
            return numTrans

        minTrans = 2147483647

        # the greedy condition where one transaction can eliminate 2 non-zero debts[i]'s
        # P.S., we need to finish the whole for loop first before we look at non-optimal choices
        for j in range(i + 1, len(debts)):
            if debts[i] + debts[j] == 0:
                debts[j] = 0
                minTrans = self.dfs(debts, i + 1, numTrans + 1)
                debts[j] = -debts[i]
                return minTrans

        for j in range(i + 1, len(debts)):
            # don't forget to check if debts[i], debts[j]'s signs are opposite
            if debts[i] * debts[j] < 0:
                debts[j] += debts[i]
                minTrans = min(minTrans, self.dfs(debts, i + 1, numTrans + 1))
                debts[j] -= debts[i]

        return minTrans


print(Solution().minTransfers([[0, 1, 10], [2, 0, 5]]))
print(Solution().minTransfers([[0, 1, 10], [1, 0, 1], [1, 2, 5], [2, 0, 5]]))
