from collections import defaultdict
from typing import List


# python has some really weird behavior of (probably) lazy array element modification -> it's known that python
# has some underlying lazy evaluation implementation.
class Solution:
    def minTransfers(self, transactions: List[List[int]]) -> int:
        netBalance = defaultdict(int)
        for i, j, amount in transactions:
            netBalance[i] -= amount
            netBalance[j] += amount

        debts = []
        for debt in netBalance.values():
            if debt != 0:
                debts.append(debt)
        debts.sort()

        return self.dfs(debts, 0)

    def dfs(self, debts: List[int], i: int) -> int:
        while i < len(debts) and debts[i] == 0:
            i += 1
        if i == len(debts):
            return 0
        # this way debts[i] won't be 0

        # try to find -debts[i] so one transaction can eliminate 2 persons
        for j in range(i + 1, len(debts)):
            if debts[j] == -debts[i]:
                debts[j] = 0
                numOfTxns = 1 + self.dfs(debts, i + 1)
                # it's really weird we have to reset this before returning.
                # if we don't reset if we will need deepcopy(debts) in the below for loop's recursion
                debts[j] = -debts[i]
                return numOfTxns

        numOfTxns = 2147483647
        # we wanna eliminate debts[i] by transferring it to j and do dfs
        for j in range(i + 1, len(debts)):
            if debts[j] * debts[i] < 0:
                debts[j] += debts[i]
                numOfTxns = min(numOfTxns, 1 + self.dfs(debts, i + 1))
                # we would have to use deepcopy here if we don't reset debts[j] in the above for loop
                debts[j] -= debts[i]

        return numOfTxns


# this is the test case for which not resetting the debts[j] will yield different result
print(Solution().minTransfers([[0, 3, 2], [1, 4, 3], [2, 3, 2], [2, 4, 2]]))
