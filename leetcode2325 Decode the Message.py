
class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        keyCharSet = set()
        orderIndexToKeyChar = {}
        orderIndex = 0
        for char in key:
            if char == ' ':
                continue
            if char not in keyCharSet:
                keyCharSet.add(char)
                orderIndexToKeyChar[orderIndex] = char
                orderIndex += 1

            if orderIndex == 26:
                break

        keyCharToOriginalChar = {}
        for i, char in enumerate('abcdefghijklmnopqrstuvwxyz'):
            keyCharToOriginalChar[orderIndexToKeyChar[i]] = char

        ans = []
        for char in message:
            if char == ' ':
                ans.append(' ')
            else:
                ans.append(keyCharToOriginalChar[char])
        return ''.join(ans)
