from typing import Dict, List

class Solution:
    def __init__(self):
        self.ans = 0

    def pathSum(self, nums: List[int]) -> int:
        self.ans = 0
        nodeToValue = {}
        for num in nums:
            value = num % 10
            node = num // 10
            nodeToValue[node] = value

        self.dfs(nodeToValue, nodeToValue[11], 11)
        return self.ans

    def dfs(self, nodeToValue: Dict[int, int], currSum: int, node: int):
        depth = node // 10
        orderInLevel = node % 10
        leftChild = (depth + 1) * 10 + 2 * orderInLevel - 1
        rightChild = (depth + 1) * 10 + 2 * orderInLevel

        # leaf node
        if depth == 4 or (leftChild not in nodeToValue and rightChild not in nodeToValue):
            self.ans += currSum
            return

        if leftChild in nodeToValue:
            self.dfs(nodeToValue, currSum + nodeToValue[leftChild], leftChild)
        if rightChild in nodeToValue:
            self.dfs(nodeToValue, currSum + nodeToValue[rightChild], rightChild)
