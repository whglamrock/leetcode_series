import math

# instead of thinking about changing the middle digit, change the whole left half
class Solution:
    def nearestPalindromic(self, n: str) -> str:
        numOfDigits = len(n)
        m = numOfDigits // 2 - 1 if numOfDigits % 2 == 0 else numOfDigits // 2
        leftHalf = int(n[:m + 1])
        n = int(n)

        candidates = []
        # left half == right half
        candidates.append(self.buildPalindromeFromLeftHalf(leftHalf, numOfDigits % 2 == 0))
        # # left half + 1
        candidates.append(self.buildPalindromeFromLeftHalf(leftHalf + 1, numOfDigits % 2 == 0))
        # # left half - 1
        candidates.append(self.buildPalindromeFromLeftHalf(leftHalf - 1, numOfDigits % 2 == 0))
        # add one digit
        candidates.append(10 ** (numOfDigits - 1) - 1)
        # minus one digit
        candidates.append(10 ** numOfDigits + 1)

        diff = math.inf
        ans = 0
        for candidate in candidates:
            if candidate == n:
                continue
            if abs(candidate - n) < diff:
                diff = abs(candidate - n)
                ans = candidate
            elif abs(candidate - n) == diff:
                ans = min(ans, candidate)

        return str(ans)

    def buildPalindromeFromLeftHalf(self, leftHalf: int, evenNumOfDigits: bool) -> int:
        leftHalfStr = str(leftHalf)
        rightHalfStr = leftHalfStr[::-1]
        if not evenNumOfDigits:
            rightHalfStr = rightHalfStr[1:]
        return int(leftHalfStr + rightHalfStr)


print(Solution().nearestPalindromic('9999'))
print(Solution().nearestPalindromic('999'))
print(Solution().nearestPalindromic('1001'))
print(Solution().nearestPalindromic('1991'))
print(Solution().nearestPalindromic('12345'))
