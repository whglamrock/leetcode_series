
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        sStack, tStack = [], []
        for char in s:
            if char == '#':
                if sStack:
                    sStack.pop()
                continue
            sStack.append(char)
        for char in t:
            if char == '#':
                if tStack:
                    tStack.pop()
                continue
            tStack.append(char)

        return sStack == tStack
