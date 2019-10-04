
# keep in mind that the arr is the IN-ORDER traversal so we cannot sort it.
# see explanation from: https://leetcode.com/problems/minimum-cost-tree-from-leaf-values/discuss/339959/One-Pass-O(N)-Time-and-Space
    # basically the question can be re-defined as: removing a[i] comes with a cost a[i] * min(a[i - 1], a[i + 1]), we
    # need to get the total cost and minimize it.
    # we always wanna remove the currently smallest one first because it will only be used once (afterwards it will always
    # be masked by bigger numbers, the reasoning behind can also be explained with the Greedy idea)

class Solution(object):
    def mctFromLeafValues(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        if not arr:
            return 0

        ans = 0
        # we can keep a decreasing stack when we find a number that's smaller than its left & right
        # putting a big number helps avoid if statement for "min(stack[-1], num)"
        stack = [2147483647]

        for num in arr:
            while stack and stack[-1] <= num:
                smallerMid = stack.pop()
                ans += smallerMid * min(stack[-1], num)
            stack.append(num)

        # > 2 not >= 2 because we need to ignore 2147483647
        while len(stack) > 2:
            ans += stack[-1] * stack[-2]
            stack.pop()

        return ans



print Solution().mctFromLeafValues([7, 12, 8, 10])
print Solution().mctFromLeafValues([7, 8, 12, 10])
