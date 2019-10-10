
class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0

        mapping = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        stack = []
        for roman in s:
            integer = mapping[roman]
            if stack and integer > stack[-1]:
                lastInteger = stack.pop()
                stack.append(integer - lastInteger)
                continue
            stack.append(integer)

        return sum(stack)



print Solution().romanToInt('D')
print Solution().romanToInt('MCMXCIV')
print Solution().romanToInt('LVIII')






