from typing import List


# It's basically impossible to figure out the solution if we don't remember the answer.
class Solution:
    def findMinMoves(self, machines: List[int]) -> int:
        total, n = sum(machines), len(machines)
        if total % n:
            return -1

        target, ans, toRight = total // n, 0, 0
        for machine in machines:
            toRight = machine + toRight - target
            ans = max(ans, abs(toRight), machine - target)
            print(toRight)

        return ans
