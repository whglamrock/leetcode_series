
# check the first two numbers, if they satisfy then check the rest
# P.S.: the second number doesn't necessarily have to be bigger than the first one.

class Solution(object):
    def isAdditiveNumber(self, num):

        if (not num) or len(num) < 3:
            return False

        i = 1
        while i < len(num):
            j = i + 1
            while j < len(num):
                start1, start2, end = 0, i, j
                #print 0, i, j
                if (num[start1] == '0' and start2 - start1 > 1) or (num[start2] == '0' and end - start2 > 1):
                    j += 1
                    continue
                while end <= len(num):
                    summary = str(int(num[start1:start2]) + int(num[start2:end]))
                    #print num[start1:start2], num[start2:end], summary
                    if num[end:end + len(summary)] == summary:
                        if end + len(summary) == len(num): return True
                        start1, start2, end = start2, end, end + len(summary)
                    else:
                        break
                if len(num) - j < j - i + 1: break
                j += 1

            i += 1

        return False



Sol = Solution()
num = "12012122436"
print Sol.isAdditiveNumber(num)
