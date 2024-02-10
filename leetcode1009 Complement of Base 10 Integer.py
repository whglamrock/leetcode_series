from collections import deque

class Solution:
    def bitwiseComplement(self, n: int) -> int:
        if n == 0:
            return 1

        binaryDigits = deque()
        while n:
            binaryDigits.appendleft(n % 2)
            n //= 2

        complementDigits = []
        for digit in binaryDigits:
            complementDigits.append(1 - digit)

        ans = 0
        for digit in complementDigits:
            ans = ans * 2 + digit

        return ans
