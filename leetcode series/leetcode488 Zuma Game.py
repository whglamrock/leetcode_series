
# brute force DFS with no memo since it's not covenient to use memo

from collections import Counter
class Solution(object):
    def findMinStep(self, board, hand):

        self.ans = 2147483647
        self.initlenofhand = len(hand)
        dic = Counter(hand)

        def helper(board, n, dic):

            if not board:
                self.ans = min(self.ans, self.initlenofhand - n)
                return

            for i, char in enumerate(board):
                if i > 0 and char == board[i - 1]:
                    continue
                j = i
                while j < len(board) and board[j] == char:
                    j += 1
                if j - i >= 3:
                    helper(board[:i] + board[j:], n, dic)
                elif j - i == 2 and dic[char] > 0:
                    dic[char] -= 1
                    helper(board[:i] + board[j:], n - 1, dic)
                    dic[char] += 1
                elif dic[char] > 0:
                    dic[char] -= 1
                    helper(board[:i] + char + board[i:], n - 1, dic)
                    dic[char] += 1

        helper(board, len(hand), dic)
        return self.ans if self.ans != 2147483647 else -1



board = "RBYYBBRRB"
hand = "YRBGB"
Sol = Solution()
print Sol.findMinStep(board, hand)
