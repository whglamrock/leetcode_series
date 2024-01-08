class Solution:
    def reverse(self, x: int) -> int:
        isNegative = False
        if x < 0:
            x = -x
            isNegative = True
        reversedInt = int(str(x)[::-1])
        if isNegative:
            reversedInt = -reversedInt

        return reversedInt if -2147483648 <= reversedInt < 2147483647 else 0
