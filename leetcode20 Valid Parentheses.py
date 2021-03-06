
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
                if dic[stack.pop()] != char:
                    return False

        return not stack



print Solution().isValid('(){[()]}()[]{}{[()]}{[()]}{}{}(')


