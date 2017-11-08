
# O(n) time, O(1) space solution

class Solution(object):
    def isOneEditDistance(self, s, t):

        if s == None or t == None:
            return False
        if abs(len(s) - len(t)) > 1:
            return False

        if len(s) == len(t):
            i = 0
            while i < len(s):
                if s[i] != t[i]:
                    break
                i += 1
            # in this case, t == s
            if i == len(s): return False
            i += 1
            while i < len(s):
                if s[i] != t[i]:
                    return False
                i += 1
            return True
        else:
            # make sure s is always longer than t
            if len(s) < len(t):
                s, t = t, s
            i = 0
            while i < len(t):
                if s[i] != t[i]:
                    break
                i += 1
            # in this case, s[:len(s) - 1] == t
            if i == len(t): return True
            while i < len(t):
                if s[i + 1] != t[i]:
                    return False
                i += 1
            return True
