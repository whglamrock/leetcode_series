
class Solution(object):
    def lengthOfLastWord(self, s):

        counter = 0
        if len(s) == 0:
            return 0
        if s[len(s)-1] == " ":
            for i in range(len(s)-1,-1,-1):
                if s[i] != " ":
                    counter += 1
                if i == 0 and counter == 0:
                    return 0
                if s[i] == " " and counter != 0:
                    return counter
        else:
            for i in range(len(s)-1,-1,-1):
                counter += 1
                if s[i] == " ":
                    counter -= 1
                    return counter

        return counter



a = 'ab '
b = Solution()
c = b.lengthOfLastWord(a)
print c





