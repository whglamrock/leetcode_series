from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.dfs(board, word, 0, i, j):
                    return True
        return False

    def dfs(self, board: List[List[str]], word: str, index: int, i: int, j: int) -> bool:
        if index == len(word) - 1:
            return word[index] == board[i][j]
        if word[index] != board[i][j]:
            return False

        # block the used element instead of using visited to save time & space
        tmp = board[i][j]
        board[i][j] = '#'
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        ans = False
        for deltaI, deltaJ in directions:
            ii, jj = i + deltaI, j + deltaJ
            if 0 <= ii < len(board) and 0 <= jj < len(board[0]):
                ans |= self.dfs(board, word, index + 1, ii, jj)

        board[i][j] = tmp
        return ans


print(Solution().exist(
    [['A', 'B', 'C', 'E'],
     ['S', 'F', 'C', 'S'],
     ['A', 'D', 'E', 'E']],
    "SEE"))
