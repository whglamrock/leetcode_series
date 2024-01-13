
# the next permutation idea: 4321 -> -1; 1342 -> 1423;
# 1) scanning digits backwards, find the first digits[i] > digits[i - 1], mark down i - 1 (j = i - 1)
# 2) find the smallest digit bigger than digits[j] in digits[i:], make it digits[k]
# 3) swap digits[j] and digits[k] and them sort digits[i:]
class Solution:
    def nextGreaterElement(self, n: int) -> int:
        digits = []
        for char in str(n):
            digits.append(int(char))

        j = -1
        for i in range(len(digits) - 1, 0, -1):
            if digits[i] > digits[i - 1]:
                j = i - 1
                break
        # digits are decreasing
        if j == -1:
            return -1

        # find the smallest digit in digits[i:] that's bigger than j
        for k in range(len(digits) - 1, i - 1, -1):
            if digits[k] > digits[j]:
                break
        digits[k], digits[j] = digits[j], digits[k]
        digits = digits[:j + 1] + sorted(digits[j + 1:])
        digits = [str(item) for item in digits]
        ans = int(''.join(digits))
        return ans if ans <= 2147483647 else -1


print(Solution().nextGreaterElement(1342))
print(Solution().nextGreaterElement(21))
print(Solution().nextGreaterElement(5))
