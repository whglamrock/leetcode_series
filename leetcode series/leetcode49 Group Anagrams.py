class Solution(object):
    def groupAnagrams(self, strs):

        dick = {}
        for i in xrange(len(strs)):
            newdick = []
            for char in strs[i]:
                newdick.append(char)
            newdick.sort()
            newitem = ''.join(newdick)
            if newitem not in dick:
                dick[newitem] = [i]
            else:
                dick[newitem].append(i)

        ans = []
        for item in dick:
            newans = []
            for index in dick[item]:
                newans.append(strs[index])
            ans.append(newans)

        return ans


Sol = Solution()
strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
print Sol.groupAnagrams(strs)
