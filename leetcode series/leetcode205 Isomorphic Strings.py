class Solution(object):
    def isIsomorphic(self, s, t):

        if len(s) != len(t):
            return False

        lst = {}
        lst2 = {}
        i = 0
        while i < len(s):
            zifu = s[i]
            zifu2 = t[i]
            if zifu not in lst:
                lst[zifu] = [i]
            else:
                lst[zifu].append(i)
            if zifu2 not in lst2:
                lst2[zifu2] = [i]
            else:
                lst2[zifu2].append(i)
            i += 1

        return sorted(lst.values())==sorted(lst2.values())

Sol = Solution()
a = 'abbc'
b = 'eeeg'
print Sol.isIsomorphic(a,b)









