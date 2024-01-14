from typing import List

# Note that the stupid LC asks for constant space and modifying the original list
class Solution:
    def compress(self, chars: List[str]) -> int:
        curr = None
        currLen = 0
        j = 0
        for i, char in enumerate(chars):
            if not curr or char != curr:
                curr = char
                currLen = 1
            else:
                currLen += 1
            if i == len(chars) - 1 or chars[i + 1] != char:
                chars[j] = curr
                j += 1
                if currLen == 1:
                    continue
                currLenStr = str(currLen)
                for k in range(len(currLenStr)):
                    chars[j] = currLenStr[k]
                    j += 1

        return j


print(Solution().compress(["a", "a", "b", "b", "1", "1", "1", "c", "c", "c", "c", "c"]))
