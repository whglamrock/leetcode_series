
class Solution(object):
    def calculate(self, s):

        stack = []
        result = 0

        # remove all white spaces:
        s = s.split(' ')
        s = ''.join(s)
        n = len(s)

        i = 0
        sign = 1    # critical when deal with the first number in a sequence
        while i < n:
            # will complete this number without using any other conditions (operators or parentheses)
            if s[i].isdigit():
                curr = [s[i]]
                while i + 1 < n and s[i + 1].isdigit():
                    curr.append(s[i + 1])
                    i += 1
                result += int(''.join(curr)) * sign
            elif s[i] == '+':
                sign = 1
            elif s[i] == '-':
                sign = -1
            elif s[i] == '(':
                stack.append(result)    # brainstorm: consider if including '*', '/' in operators
                stack.append(sign)
                result = 0
                sign = 1    # add a virtual "+" for the 1st number of a new sequence
            else:
                # first stack.pop() is the previous sign that related to the current "result"
                # second stack.pop() is the previously calculated number
                result = stack.pop() * result + stack.pop()
            i += 1

        return result



sol = Solution()
s = "(1+(4+5+2)-3)+(6+8)"
print sol.calculate(s)





