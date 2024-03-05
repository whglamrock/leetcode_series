from collections import defaultdict
from copy import deepcopy
from typing import List, Dict

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        todo = {('', 0)}
        visited = set()
        workingNumCountStrs = set()
        while todo:
            nextTodo = set()
            for serializedNumCount, currSum in todo:
                visited.add(serializedNumCount)
                if currSum == target:
                    workingNumCountStrs.add(serializedNumCount)
                    continue

                numCount = self.deserializeToNumCount(serializedNumCount)
                for nextNum in candidates:
                    if currSum + nextNum > target:
                        continue
                    nextNumCount = deepcopy(numCount)
                    nextNumCount[nextNum] += 1
                    serializedNexNumCount = self.serializeNumCount(nextNumCount)
                    if serializedNexNumCount in visited:
                        continue
                    visited.add(serializedNexNumCount)
                    nextSum = currSum + nextNum
                    nextTodo.add((serializedNexNumCount, nextSum))

            todo = nextTodo

        ans = []
        for numCountStr in workingNumCountStrs:
            numCount = self.deserializeToNumCount(numCountStr)
            curr = []
            for num in numCount:
                for i in range(numCount[num]):
                    curr.append(num)
            ans.append(curr)

        return ans

    def serializeNumCount(self, numCount: Dict[int, int]) -> str:
        sortedNums = sorted(numCount.keys())
        serialized = []
        for num in sortedNums:
            serialized.append(str(num) + ':' + str(numCount[num]))
        return ','.join(serialized)

    def deserializeToNumCount(self, numCountStr: str) -> Dict[int, int]:
        if not numCountStr:
            return defaultdict(int)

        tokens = numCountStr.split(',')
        numCount = defaultdict(int)
        for token in tokens:
            splitterIndex = token.index(':')
            num = int(token[:splitterIndex])
            count = int(token[splitterIndex + 1:])
            numCount[num] = count
        return numCount
