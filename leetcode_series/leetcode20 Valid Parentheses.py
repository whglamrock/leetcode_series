
class Solution(object):
    def isValid(self, s):

        fanhui = True
        i = 0
        lst = []
        for j in range(len(s)):
            lst.append(s[j])
        if len(lst)%2 != 0:
            fanhui = False

        while i+1 < len(lst):
            if lst[i] == '(' and lst[i+1] == ')':
                del lst[i]
                del lst[i]
                if i > 0:
                    i -= 1
            elif lst[i] == '[' and lst[i+1] == ']':
                del lst[i]
                del lst[i]
                if i > 0:
                    i -= 1
            elif lst[i] == '{' and lst[i+1] == '}':
                del lst[i]
                del lst[i]
                if i > 0:
                    i -= 1
            else:
                i += 1

        if len(lst) != 0:
            fanhui = False
        return fanhui



atr = '(){[()]}()[]{}{[()]}{[()]}{}{}('
a = Solution()
print a.isValid(atr)


