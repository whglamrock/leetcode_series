# O(n) time, O(1) space solution
class Solution(object):
    def isOneEditDistance(self, s, t):

        if s == None or t == None:
            return False
        if abs(len(s) - len(t)) > 1:
            return False

        if len(s) == len(t):
            count = 0
            for i in xrange(len(s)):
                if s[i] != t[i]:
                    count += 1
                    if count > 1:
                        return False
            if count == 1:
                return True
            else:
                return False
        elif len(s) == len(t) + 1:
            i = 0
            while i < len(t) and s[i] == t[i]:
                i += 1
            i += 1
            while i < len(s):
                if s[i] != t[i - 1]:
                    return False
                i += 1
            return True
        elif len(t) == len(s) + 1:
            i = 0
            while i < len(s) and s[i] == t[i]:
                i += 1
            i += 1
            while i < len(t):
                if t[i] != s[i - 1]:
                    return False
                i += 1
            return True
        else:
            return False

