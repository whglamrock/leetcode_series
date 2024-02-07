from typing import List

# This is such a stupid question and the stupid fucking leetcode basically forces you to use binary search.
# In real interview, if it takes 15 mins to even read & understand the question, the bruteforce solution is definitely ok
class Solution:
    def maxNumberOfAlloys(self, n: int, k: int, budget: int, composition: List[List[int]], stock: List[int], cost: List[int]) -> int:
        l, r = 0, 10 ** 9 // min(cost)
        while l <= r:
            m = (l + r + 1) // 2
            if l == r:
                if self.isBudgetEnoughToBuild(m, budget, composition, stock, cost):
                    return m
                return 0
            if self.isBudgetEnoughToBuild(m, budget, composition, stock, cost):
                l = m
            else:
                r = m - 1

        return l

    def isBudgetEnoughToBuild(self, m: int, budget: int, composition: List[List[int]], stock: List[int], cost: List[int]) -> bool:
        minCost = 2147483647
        for i in range(len(composition)):
            currCost = 0
            for j in range(len(composition[0])):
                if stock[j] >= composition[i][j] * m:
                    continue
                currCost += (composition[i][j] * m - stock[j]) * cost[j]
            minCost = min(minCost, currCost)
        return minCost <= budget


'''
from copy import deepcopy

# original brute force solution
class Solution:
    def maxNumberOfAlloys(self, n: int, k: int, budget: int, composition: List[List[int]], stock: List[int], cost: List[int]) -> int:
        maxNumOfAlloy = 0
        for i in range(len(composition)):
            stockCopy = deepcopy(stock)
            budgetCopy = budget
            numOfAlloyFromStock = self.numOfAlloysFromStocks(composition, stockCopy, i)
            for j in range(len(stock)):
                stockCopy[j] -= numOfAlloyFromStock * composition[i][j]
            numOfAlloyFromBudget = self.numOfAlloysWithBudget(budgetCopy, composition, stockCopy, cost, i)
            numOfAlloys = numOfAlloyFromStock + numOfAlloyFromBudget
            maxNumOfAlloy = max(maxNumOfAlloy, numOfAlloys)
        
        return maxNumOfAlloy
        
    # it's assumed that we have used up the stock to build alloy already
    def numOfAlloysWithBudget(self, budget: int, composition: List[List[int]], stock: List[int], cost: List[int], i: int) -> int:
        costToBuyMetals = 0
        for j in range(len(composition[0])):
            if stock[j] < composition[i][j]:
                costToBuyMetals += cost[j] * (composition[i][j] - stock[j])
                stock[j] = 0
            else:
                stock[j] -= composition[i][j]

        numOfAlloys = 0
        while budget >= costToBuyMetals:
            numOfAlloys += 1
            budget -= costToBuyMetals
            costToBuyMetals = 0
            for j in range(len(composition[0])):
                if stock[j] < composition[i][j]:
                    costToBuyMetals += cost[j] * (composition[i][j] - stock[j])
                    stock[j] = 0
                else:
                    stock[j] -= composition[i][j]
        
        return numOfAlloys

    def numOfAlloysFromStocks(self, composition: List[List[int]], stock: List[int], i: int) -> int:
        minNumOfAlloys = 2147483647
        for j in range(len(composition[0])):
            minNumOfAlloys = min(minNumOfAlloys, stock[j] // composition[i][j])
        return minNumOfAlloys
'''