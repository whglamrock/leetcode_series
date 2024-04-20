from typing import List

# Note that the stupid LC asks for constant space and modifying the original list
class Solution:
    def compress(self, chars: List[str]) -> int:
        # i is the slow index, j is the fast index
        i, j, n = 0, 0, len(chars)
        while i < n and j < n:
            # always reset the currChar
            currChar = chars[j]
            startingIndex = j
            while j < n and chars[j] == currChar:
                j += 1
            count = j - startingIndex

            chars[i] = currChar
            # move the slow index +1, to either assign the count value or the next char
            i += 1
            if count == 1:
                continue

            for digit in str(count):
                chars[i] = digit
                i += 1

        return i


chars = ["a", "a", "b", "b", "1", "1", "1", "c", "c", "c", "c", "c"]
print(chars[:Solution().compress(chars)])
