from typing import List

# the problem description appeared to be super vague.
# need to ask more questions in real interview.
class Solution(object):
    def validUtf8(self, data: List[int]) -> bool:

        bitCount = 0

        for n in data:
            if n >= 192:
                if bitCount != 0:
                    return False
                if n >= 240:
                    bitCount = 3
                elif n >= 224:
                    bitCount = 2
                else:
                    bitCount = 1
            elif n >= 128:
                bitCount -= 1
                if bitCount < 0:
                    return False
            elif bitCount > 0:
                return False

        return bitCount == 0
