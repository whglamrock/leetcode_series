
# O(1) math solution.
# Idea: for target = 9, we take smaller pairwise numbers 1, 2, 3, 4 and discard 5, 6, 7, 8. Then based on n, if we
# lack numbers we take from integers >= target. Note that the number of bigger pairwise numbers is not target // 2
# because for even target like target = 8, the bigger pairwise numbers are 5, 6, 7 (note that 4 can also be used in
# beautiful array based on problem definition).
class Solution:
    def minimumPossibleSum(self, n: int, target: int) -> int:
        if n <= target // 2:
            ans = (1 + n) * n // 2
        elif n <= target - 1:
            numOfSmallerPairwiseNumbers = target // 2
            numOfBiggerPairwiseNumbers = n - numOfSmallerPairwiseNumbers
            ans = (1 + numOfSmallerPairwiseNumbers) * numOfSmallerPairwiseNumbers // 2 + (target + target + numOfBiggerPairwiseNumbers - 1) * numOfBiggerPairwiseNumbers // 2
        else:
            numOfSmallerPairwiseNumbers = target // 2
            numOfBiggerPairwiseNumbers = target - numOfSmallerPairwiseNumbers - 1
            # n - target + 1 is how many extra increased numbers we need after compensating all removed bigger pairwise numbers
            numOfIncreasedNumbers = numOfBiggerPairwiseNumbers + n - target + 1
            ans = (1 + numOfSmallerPairwiseNumbers) * numOfSmallerPairwiseNumbers // 2 + (target + target + numOfIncreasedNumbers - 1) * numOfIncreasedNumbers // 2

        return ans % (10 ** 9 + 7)
