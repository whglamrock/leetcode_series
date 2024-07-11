from typing import List


# we need a stack to store the functions, there is no way to avoid that
class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        ans = [0] * n
        currStart = 0
        stack = []

        for log in logs:
            function, operation, time = log.split(':')
            function, time = int(function), int(time)
            if operation == 'start':
                if stack:
                    ans[stack[-1]] += time - currStart
                stack.append(function)
                currStart = time
            else:
                stack.pop()
                ans[function] += time - currStart + 1
                currStart = time + 1

        return ans


print(Solution().exclusiveTime(2, ["0:start:0", "1:start:2", "1:end:5", "0:end:6"]))
