from copy import deepcopy
from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        todo = [[]]
        for num in nums:
            nextTodo = deepcopy(todo)
            for subset in todo:
                nextTodo.append(subset + [num])
            todo = nextTodo
        return todo


print(Solution().subsets([2, 1, 4, 3, 5]))
