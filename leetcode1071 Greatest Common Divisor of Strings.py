
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if len(str1) < len(str2):
            str1, str2 = str2, str1

        commonPrefix = []
        for i in range(len(str2)):
            if str1[i] != str2[i]:
                break
            commonPrefix.append(str2[i])
        commonPrefix = ''.join(commonPrefix)

        if not commonPrefix:
            return ''

        for i in range(len(commonPrefix), 0, -1):
            currPrefix = commonPrefix[:i]
            if self.isDividable(str1, currPrefix) and self.isDividable(str2, currPrefix):
                return currPrefix
        return ''

    def isDividable(self, s: str, substr: str) -> bool:
        k = len(substr)
        if len(s) % k != 0:
            return False

        for i in range(0, len(s) - k + 1, k):
            if s[i:i + k] != substr:
                return False
        return True
