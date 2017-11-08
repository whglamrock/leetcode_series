
# only lowercase letters are assumed in each string

class Solution(object):
    def groupStrings(self, strings):

        patterns = {}
        for word in strings:
            if len(word) == 1:
                if ' ' not in patterns: patterns[' '] = []
                patterns[' '].append(word)
                continue
            pat = []
            for j in xrange(1, len(word)):
                pat.append(str((ord(word[j]) - ord(word[j - 1]) + 26) % 26))
            key = ' '.join(pat)
            if key not in patterns: patterns[key] = []
            patterns[key].append(word)

        ans = []
        for list in patterns.values():
            ans.append(list)

        return ans



strings = ["abc", "bcd", "acef", "xyz", "az", "ba", "a", "z"]
Sol = Solution()
print Sol.groupStrings(strings)



'''
# Original Solution (not efficient)

class Solution(object):
    def groupStrings(self, strings):

        def judge(str1, str2):
            if len(str1) != len(str2):
                return False
            else:
                for i in xrange(len(str1)-1):
                    distance1, distance2 =  ord(str1[i]) - ord(str1[i+1]), ord(str2[i]) - ord(str2[i+1])
                    if distance1 != distance2:
                        if abs(distance1-distance2) == 26 :
                            continue
                        else:
                            return False
            return True

        ans = []
        while strings:
            i = 0
            ans1 = [strings.pop(0)]
            while i<len(strings):
                if judge(strings[i], ans1[0]) == True:
                    ans1.append(strings.pop(i))
                    continue
                else:
                    i += 1
            ans1.sort()
            ans.append(ans1)

        return ans
'''




