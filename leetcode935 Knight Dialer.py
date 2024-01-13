
# O(n) dp solution, good enough for interview. No need for O(logN) solution.
class Solution:
    def knightDialer(self, n: int) -> int:
        neighbors = {
            0: [4, 6],
            1: [6, 8],
            2: [7, 9],
            3: [4, 8],
            4: [0, 3, 9],
            5: [],
            6: [0, 1, 7],
            7: [2, 6],
            8: [1, 3],
            9: [2, 4]
        }
        mod = 10 ** 9 + 7
        currCounts = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        for i in range(n - 1):
            nextCounts = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
            for src in range(10):
                for dest in neighbors[src]:
                    nextCounts[dest] = (nextCounts[dest] + currCounts[src]) % mod
            currCounts = nextCounts
            # print(currCounts)
        return sum(currCounts) % mod


print(Solution().knightDialer(3))
print(Solution().knightDialer(4))
