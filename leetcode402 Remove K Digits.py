
# the idea is actually greedy algorithm
# think about the edge case when we have 0 and tight in num

class Solution(object):
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        # increasing stack
        stack = []
        for digit in num:
            while stack and k and int(stack[-1]) > int(digit):
                stack.pop()
                k -= 1
            stack.append(digit)

        while k:
            stack.pop()
            k -= 1

        ans = ''.join(stack).lstrip('0')
        # consider edge case like '10, k = 1'
        return ans if ans else '0'



print Solution().removeKdigits('100243210', 3)
print Solution().removeKdigits('1432219', 2)
print Solution().removeKdigits('3813471349', 4)
print Solution().removeKdigits('1112223', 3)
print Solution().removeKdigits('10', 1)

