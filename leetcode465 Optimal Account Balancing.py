from collections import defaultdict
from typing import List

# python has some really weird behavior of (probably) lazy array element modification -> it's known that python
# has some underlying lazy evaluation implementation.
class Solution:
    def minTransfers(self, transactions: List[List[int]]) -> int:
        netBalances = defaultdict(int)
        for i, j, amount in transactions:
            netBalances[i] -= amount
            netBalances[j] += amount

        debts = []
        for balance in netBalances.values():
            if balance != 0:
                debts.append(balance)

        return self.dfs(debts, 0, 0)

    def dfs(self, debts: List[int], i: int, currTxns: int) -> int:
        while i < len(debts) and debts[i] == 0:
            i += 1
        if i == len(debts):
            return currTxns
        # this way debts[i] won't be 0

        minTxns = 2147483647
        # try to find -debts[i] so one transaction can eliminate 2 persons
        for j in range(i + 1, len(debts)):
            if debts[j] + debts[i] == 0:
                debts[j] = 0
                minTxns = self.dfs(debts, i + 1, currTxns + 1)
                # it's really weird we have to reset this before returning.
                # if we don't reset if we will need deepcopy(debts) in the below for loop's recursion
                debts[j] = -debts[i]
                return minTxns

        # we wanna eliminate debts[i] by transferring it to j and do dfs
        for j in range(i + 1, len(debts)):
            if debts[j] * debts[i] < 0:
                debts[j] += debts[i]
                # we would have to use deepcopy here if we don't reset debts[j] in above for loop
                minTxns = min(minTxns, self.dfs(debts, i + 1, currTxns + 1))
                debts[j] -= debts[i]

        return minTxns


# this is the test case for which not resetting the debts[j] will yield different result
print(Solution().minTransfers([[0, 3, 2], [1, 4, 3], [2, 3, 2], [2, 4, 2]]))
