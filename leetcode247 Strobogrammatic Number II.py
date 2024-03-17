from typing import List

class Solution:
    def findStrobogrammatic(self, n: int) -> List[str]:
        if n == 1:
            return ["0", "1", "8"]
        if n == 2:
            return ["11", "69", "88", "96"]

        if n % 2:
            # middle digit can't be 6 or 9
            todo = {'1', '0', '8'}
        else:
            todo = {''}

        for i in range(n // 2):
            nextTodo = set()
            for item in todo:
                nextTodo.add('0' + item + '0')
                nextTodo.add('1' + item + '1')
                nextTodo.add('8' + item + '8')
                nextTodo.add('6' + item + '9')
                nextTodo.add('9' + item + '6')
            todo = nextTodo

        ans = []
        for num in todo:
            if not num.startswith('0'):
                ans.append(num)
        return ans


print(Solution().findStrobogrammatic(5))
