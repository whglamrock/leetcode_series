from typing import List

# 1) We have to use a stack to store the started/ongoing functions instead of using a "executionFunction" single variable
# to record the start function. Because for every operation you will need to switch context, in which case you will
# lose track of which function you should execute (i.e., the "executionFunction" may point to the wrong function).
# 2) We also need a currStartTime variable to record/reset the new start time, especially when a function ends and
# we need to restart executing the function on top of the stack. If we simply store the original start time in the stack
# that original start time != currStartTime and will result in wrong execution time calculation.
class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        stack = []
        ans = [0] * n
        currStartTime = 0

        for log in logs:
            function, operation, time = log.split(':')
            function, time = int(function), int(time)
            if operation == 'start':
                if stack:
                    ans[stack[-1]] += time - currStartTime
                stack.append(function)
                currStartTime = time
            else:
                ans[stack[-1]] += time - currStartTime + 1
                stack.pop()
                currStartTime = time + 1

        return ans


print(Solution().exclusiveTime(2, ["0:start:0", "1:start:2", "1:end:5", "0:end:6"]))
