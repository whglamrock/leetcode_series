class Solution(object):
    def isAnagram(self, s, t):

        if len(s) != len(t):
            return False

        dick = {}
        fuck = {}
        for item in s:
            if item not in dick:
                dick[item] = [0]
            else:
                dick[item].append(0)

        for item in t:
            if item not in fuck:
                fuck[item] = [0]
            else:
                fuck[item].append(0)

        return fuck == dick # when compare by hash table, it's always faster than for loop.

#        for item in s:
#            if item not in t:
#                return False
#            else:
#                if len(dick[item]) != len(fuck[item]):
#                    return False
#
#        return True

a = 'ab'
b = 'ba'

Sol = Solution()
print Sol.isAnagram(a,b)
