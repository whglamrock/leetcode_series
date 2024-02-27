
# We only add 'R' to the stack as if it's an open parenthesis (i.e., like a '(', yeah).
class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        n = len(dominoes)
        stack = []
        ans = [''] * n
        for i, char in enumerate(dominoes):
            if char == '.':
                continue
            if char == 'R':
                # dominoes in between i and previously updated index remain upright
                if not stack:
                    j = i - 1
                    while j >= 0 and not ans[j]:
                        ans[j] = '.'
                        j -= 1
                # extend the state rightward
                elif stack and stack[-1][1] == 'R':
                    prevIndexOfR = stack.pop()[0]
                    j = prevIndexOfR - 1
                    while j >= 0 and not ans[j]:
                        ans[j] = '.'
                        j -= 1
                    for j in range(prevIndexOfR, i + 1):
                        ans[j] = 'R'
                stack.append([i, char])
            else:
                if stack and stack[-1][1] == 'R':
                    prevIndexOfR = stack.pop()[0]
                    if (i - prevIndexOfR) % 2 == 0:
                        middlePoint = (i + prevIndexOfR) // 2
                        for j in range(prevIndexOfR, middlePoint):
                            ans[j] = 'R'
                        ans[middlePoint] = '.'
                        for j in range(middlePoint + 1, i + 1):
                            ans[j] = 'L'
                    else:
                        diff = i - prevIndexOfR
                        for j in range(prevIndexOfR, prevIndexOfR + diff // 2 + 1):
                            ans[j] = 'R'
                        for j in range(i - diff // 2, i + 1):
                            ans[j] = 'L'
                # no matter what previous index is, it doesn't matter, dominoes fall left all the way
                else:
                    j = i
                    while j >= 0 and not ans[j]:
                        ans[j] = 'L'
                        j -= 1

        # there is an 'R' left in stack
        if stack:
            prevIndexOfR = stack.pop()[0]
            j = prevIndexOfR - 1
            while j >= 0 and not ans[j]:
                ans[j] = '.'
                j -= 1
            for j in range(prevIndexOfR, n):
                ans[j] = 'R'

        # in case the previous index is 'L' or there is no push at all
        j = len(ans) - 1
        while j >= 0 and not ans[j]:
            ans[j] = '.'
            j -= 1

        return ''.join(ans)
