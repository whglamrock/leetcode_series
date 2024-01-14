from typing import List

# O(target * n^2) time complexity
class Solution:
    def minimizeTheDifference(self, mat: List[List[int]], target: int) -> int:
        minSum = sum(min(row) for row in mat)
        if minSum > target:
            return minSum - target

        # because we need to find min absolute diff, target - minSum is already a candidate
        # we need to some sum > target so that sum - target < target - minSum.
        todo = {0}
        for row in mat:
            nextTodo = set()
            for num in row:
                for currSum in todo:
                    # so that at any time, the nextTodo set won't contain more than 2 * target numbers
                    if currSum + num < 2 * target - minSum:
                        nextTodo.add(currSum + num)
            todo = nextTodo

        ans = target - minSum
        for possibleSum in todo:
            ans = min(ans, abs(target - possibleSum))
        return ans


print(Solution().minimizeTheDifference(mat=[[1, 2, 3], [4, 5, 6], [7, 8, 9]], target=13))
