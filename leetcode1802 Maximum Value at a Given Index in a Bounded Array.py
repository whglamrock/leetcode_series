from math import floor, sqrt

# This is a stupid math problem.
# Idea:
# 1) We first put 1 at each index, and try to add 1 to index and it's neighbors, extending leftward and rightward.
# e.g., with n = 6 and index = 2, we first have: 1 1 1 1 1 1
# then we try to add 1's on left and right side until we can't:
# 1 1 1 1 1 1 -> 1 1 1 1 1 1 -> 1 1 1 1 1 1 ->
#     1            1 1 1        1 1 1 1 1
#                    1            1 1 1
#                                   1
# 2) At this point, the length of next layer of 1's can only be 1 more than the previous layer (not 2 more, like previously)
# 3) We define the scenario in 1) as "equal edge" where each layer extends same number of ones leftward & rightward from index
# we calculate the total number of ones in equal edge case
# 4) For unequal one layer:
# 1 1 1 1 1 1 -> 1 1 1 1 1 1 -> ...
# 1 1 1 1 1      1 1 1 1 1 1
#   1 1 1        1 1 1 1 1
#     1            1 1 1
#                    1
# 5) in the above case, the first unequal edge layer has 6 1's which already == n. but if it's < n we need to increase
# the length of such layer by 1 until it's == n. We then calculate the total number ones in unequal edge case
# 6) If there's still non 0 maxSum left, we try to add layer of length n to the pile.
class Solution:
    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        maxSum -= n

        maxEqualEdge = min(index, n - index - 1)
        maxRegularNumOfOnesToAdd = 1 + 2 * maxEqualEdge
        sumOfEqualEdgeOnes = (1 + maxRegularNumOfOnesToAdd) ** 2 // 4
        if maxSum <= sumOfEqualEdgeOnes:
            return 1 + floor(sqrt(maxSum))

        heightOfEqualEdgeOnes = (maxRegularNumOfOnesToAdd + 1) // 2
        maxSum -= sumOfEqualEdgeOnes
        sumOfUnequalEdgeOnes = (maxRegularNumOfOnesToAdd + 1 + n) * (n - maxRegularNumOfOnesToAdd) // 2
        if maxSum <= sumOfUnequalEdgeOnes:
            x = floor(sqrt(maxRegularNumOfOnesToAdd * maxRegularNumOfOnesToAdd + maxRegularNumOfOnesToAdd + 2 * maxSum))
            if x * (x + 1) > maxRegularNumOfOnesToAdd * maxRegularNumOfOnesToAdd + maxRegularNumOfOnesToAdd + 2 * maxSum:
                x -= 1
            return 1 + heightOfEqualEdgeOnes + (x - maxRegularNumOfOnesToAdd)

        heightOfUnequalEdgeOnes = n - maxRegularNumOfOnesToAdd
        maxSum -= sumOfUnequalEdgeOnes
        return 1 + heightOfEqualEdgeOnes + heightOfUnequalEdgeOnes + maxSum // n
