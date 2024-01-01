
class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        numOfAsCanBeRemoved = 0
        numOfBsCanBeRemoved = 0
        for i in range(1, len(colors) - 1):
            if colors[i] == colors[i - 1] == colors[i + 1] == 'A':
                numOfAsCanBeRemoved += 1
            elif colors[i] == colors[i - 1] == colors[i + 1] == 'B':
                numOfBsCanBeRemoved += 1

        return numOfAsCanBeRemoved > numOfBsCanBeRemoved


print(Solution().winnerOfGame(colors="AAABABB"))
print(Solution().winnerOfGame(colors="AA"))
print(Solution().winnerOfGame(colors="ABBBBBBBAAA"))
