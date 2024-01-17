class Solution(object):
    def numSquares(self, n: int) -> int:

        if n < 4:
            return n

        squareNumbers = []
        i = 1
        while i * i <= n:
            squareNumbers.append(i * i)
            i += 1

        todo = {n}
        count = 0
        while todo:
            count += 1
            nextTodo = set()
            for target in todo:
                for squareNum in squareNumbers:
                    if target == squareNum:
                        return count
                    # because squareNumbers is a sorted list
                    elif target < squareNum:
                        break
                    nextTodo.add(target - squareNum)
            todo = nextTodo

        return count


'''
# O(N * N) dp solution that should get accepted in real interview but got TLE in stupid leetcode
class Solution:
    def numSquares(self, n: int) -> int:
        if n == 1:
            return 1

        squareNumbers = set()
        for i in range(1, floor(sqrt(n)) + 1):
            squareNumbers.add(i * i)
        
        dp = [0] * (n + 1)
        for num in squareNumbers:
            dp[num] = 1
        
        for i in range(2, n + 1):
            for j in range(i):
                if dp[j] > 0 and i - j in squareNumbers:
                    if dp[i] != 0:
                        dp[i] = min(dp[i], dp[j] + 1)
                    else:
                        dp[i] = dp[j] + 1

        return dp[-1]
'''