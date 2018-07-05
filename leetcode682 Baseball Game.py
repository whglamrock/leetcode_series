
class Solution(object):
    def calPoints(self, ops):

        stack = []
        for string in ops:
            if string == 'C':
                stack.pop()
            elif string == 'D':
                if stack:
                    stack.append(stack[-1] * 2)
            elif string == '+':
                if len(stack) >= 2:
                    stack.append(stack[-1] + stack[-2])
            else:
                stack.append(int(string))

        return sum(stack)



Sol = Solution()
ops = ["5","-2","4","C","D","9","+","+"]
print Sol.calPoints(ops)
