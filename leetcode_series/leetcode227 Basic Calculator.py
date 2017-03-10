class Solution(object):
    def calculate(self, s):

        operators = {"+", "-", "*", "/"}
        i = 0
        stack = []
        num = ''

        while i < len(s):
            if s[i] in operators:
                if num:
                    stack.append(int(num))
                    num = ''
                stack.append(s[i])
            else:
                if s[i] != ' ':
                    num += s[i]    # for number contains more than one digit
            i += 1
            if i == len(s) and num:
                stack.append(int(num))
        # parse the s

        traversal = []
        i = 0
        while i < len(stack):
            if stack[i] == '*':
                leftnum = traversal.pop()
                rightnum = stack[i+1]
                traversal.append(leftnum * rightnum)
                i += 2
            elif stack[i] == '/':
                leftnum = traversal.pop()
                rightnum = stack[i+1]
                traversal.append(leftnum / rightnum)
                i += 2
            else:
                traversal.append(stack[i])
                i += 1

        ans = traversal[0]
        for i in xrange(1, len(traversal)-1, 2):
            if traversal[i] == '+':
                ans += traversal[i+1]
            else:
                ans -= traversal[i+1]

        return ans