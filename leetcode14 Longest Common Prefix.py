
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ''
        if len(strs) == 1:
            return strs[0]

        ans = strs[0]
        for i in xrange(1, len(strs)):
            string = strs[i]
            commonPrefix = self.getCommonPrefix(string, ans)
            if not commonPrefix:
                return ''
            ans = commonPrefix

        return ans

    def getCommonPrefix(self, str1, str2):
        i = 0
        commonPrefix = []
        while i < min(len(str1), len(str2)):
            if str1[i] != str2[i]:
                break
            commonPrefix.append(str1[i])
            i += 1
        return ''.join(commonPrefix)



print Solution().longestCommonPrefix(["flower", "flow", "flight"])
print Solution().longestCommonPrefix(["dog", "racecar", "car"])