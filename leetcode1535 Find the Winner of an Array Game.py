from typing import List

# after the biggest integer is moved to arr[0], it will keep winning
class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        increasingElements = []
        for i, num in enumerate(arr):
            if not increasingElements or num > increasingElements[-1][1]:
                increasingElements.append([i, num])

        for i in range(len(increasingElements) - 1):
            gameCanWin = increasingElements[i + 1][0] - increasingElements[i][0] - 1
            if i > 0:
                # i can beat its left
                gameCanWin += 1
            if gameCanWin >= k:
                return increasingElements[i][1]

        # at this point we know only the biggest number can win
        return increasingElements[-1][1]


print(Solution().getWinner([2, 1, 3, 5, 4, 6, 7], 2))
print(Solution().getWinner([3, 2, 1], 10))
print(Solution().getWinner([2, 1, 3, 5, 4, 8, 7, 20, 18, 16, 24, 21, 11, 15, 10, 14], 100))
