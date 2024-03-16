
# optimal O(n) solution: scanning backward, record the index of the max digit seen so far; then try to find
# the left most digit < the max digit seen so far
class Solution:
    def maximumSwap(self, num: int) -> int:
        num = [int(digit) for digit in str(num)]
        maxIndex = len(num) - 1
        left, right = 0, 0
        for i in range(len(num) - 1, -1, -1):
            if num[i] > num[maxIndex]:
                maxIndex = i
            elif num[i] < num[maxIndex]:
                left = i
                right = maxIndex

        num[left], num[right] = num[right], num[left]
        return int(''.join([str(digit) for digit in num]))


'''
# straightforward sorting solution, O(n * log(n)) time. num has at most 8 digits so it's also fine to use this
# solution in real interview.
class Solution:
    def maximumSwap(self, num: int) -> int:
        digits = []
        digitToIndex = {}
        originalNum = str(num)
        for i, char in enumerate(str(num)):
            digits.append(int(char))
            digitToIndex[int(char)] = i
        digits.sort(reverse=True)

        for i, digit in enumerate(digits):
            originalDigit = int(originalNum[i])
            if originalDigit == digit:
                continue
            # found the digit to swap
            j = digitToIndex[digit]
            return int(originalNum[:i] + str(digit) + originalNum[i + 1:j] + str(originalDigit) + originalNum[j + 1:])

        return int(originalNum)
'''