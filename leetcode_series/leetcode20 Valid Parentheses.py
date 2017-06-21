
class Solution(object):
    def isValid(self, s):

        if not s:
            return True
        if len(s) % 2 != 0:
            return False

        dic = {'(': ')', '[': ']', '{': '}'}
        stack = []

        for char in s:
            if char in dic:
                stack.append(char)
            elif not stack:
                return False
            else:
                lastchar = stack.pop()
                if lastchar not in dic or dic[lastchar] != char:
                    return False

        return len(stack) == 0



s = '(){[()]}()[]{}{[()]}{[()]}{}{}('
Sol = Solution()
print Sol.isValid(s)


