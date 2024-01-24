from collections import deque
from typing import List

class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        bitsOfA = self.getBits(a)
        bitsOfB = self.getBits(b)
        bitsOfC = self.getBits(c)
        maxNumOfDigits = max(len(bitsOfA), len(bitsOfB), len(bitsOfC))
        while len(bitsOfA) < maxNumOfDigits:
            bitsOfA.appendleft(0)
        while len(bitsOfB) < maxNumOfDigits:
            bitsOfB.appendleft(0)
        while len(bitsOfC) < maxNumOfDigits:
            bitsOfC.appendleft(0)

        numOfFlips = 0
        for i in range(maxNumOfDigits):
            if bitsOfA[i] == bitsOfB[i] == bitsOfC[i]:
                continue
            if bitsOfC[i] == 1:
                if bitsOfA[i] == bitsOfB[i] == 0:
                    numOfFlips += 1
            else:
                if bitsOfA[i] == bitsOfB[i] == 1:
                    numOfFlips += 2
                elif bitsOfA[i] == 1 or bitsOfB[i] == 1:
                    numOfFlips += 1

        return numOfFlips

    def getBits(self, num: int) -> List[int]:
        bits = deque()
        while num:
            bits.appendleft(num % 2)
            num //= 2

        return bits


print(Solution().minFlips(a=2, b=6, c=5))
print(Solution().minFlips(a=4, b=2, c=7))
