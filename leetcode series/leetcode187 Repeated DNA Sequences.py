# O(n) time/space solution
class Solution(object):
    def findRepeatedDnaSequences(self, s):
        dick = {}
        ans = []
        i = 0
        while i + 10 <= len(s):
            if s[i: i+10] not in dick:
                dick[s[i: i+10]] = 1
            else:
                dick[s[i: i+10]] += 1
            i += 1

        for item in dick:
            if dick[item] > 1:
                ans.append(item)

        return ans