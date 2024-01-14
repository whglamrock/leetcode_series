from collections import defaultdict, deque

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        chars = deque()
        for char in s:
            chars.append(char)

        col = 0
        colToChars = defaultdict(deque)
        while chars:
            # the column where it's all chars
            for i in range(min(numRows, len(chars))):
                colToChars[col].append(chars.popleft())
            col += 1
            # the zip zag columns
            for i in range(numRows - 2):
                if not chars:
                    break
                for j in range(numRows - 1 - i - 1):
                    colToChars[col].append(' ')
                colToChars[col].append(chars.popleft())
                for j in range(i + 1):
                    colToChars[col].append(' ')
                col += 1

        maxCol = max(colToChars.keys())
        rows = []
        for i in range(numRows):
            row = []
            for j in range(maxCol + 1):
                if colToChars[j]:
                    char = colToChars[j].popleft()
                    if char != ' ':
                        row.append(char)
                    if not colToChars[j]:
                        del colToChars[j]
            rows.append(''.join(row))

        return ''.join(rows)


print(Solution().convert(s="PAYPALISHIRING", numRows=3))
print(Solution().convert(s="PAYPALISHIRING", numRows=4))
