# an elegant stack solution
# we have to use list to preserve the char and join them afterwards because string
# is immutable in python.
class Solution(object):
    def decodeString(self, s):

        stack = [[[], 1]]   # very important!
        num = []
        for ch in s:
            if ch.isdigit():
                num.append(ch)
            elif ch == '[':
                stack.append([[], int(''.join(num))])
                num = []
            elif ch == ']':
                string, k = stack.pop()
                string = ''.join(string)
                for i in xrange(k):
                    stack[-1][0].append(string)
            else:
                stack[-1][0].append(ch)
            #print stack

        return ''.join(stack[0][0])


s = '3[a2[c]]ef'
Sol = Solution()
print Sol.decodeString(s)



