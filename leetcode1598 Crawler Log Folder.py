from typing import List


class Solution:
    def minOperations(self, logs: List[str]) -> int:
        stack = []
        for log in logs:
            folder = log[:len(log) - 1]
            if folder == '.':
                continue

            if folder == '..':
                if stack:
                    stack.pop()
            else:
                stack.append(folder)

        return len(stack)
