
# Pay attention to the way of backtracking

class Solution(object):
    def generateAbbreviations(self, word):

        if not word:
            return ['']

        ans = []
        for i in xrange(len(word)):
            next = []
            if i == 0:
                next.append(word[0])
                next.append('1')
            else:
                for sub in ans:
                    if sub[-1].isdigit():
                        j = len(sub) - 1
                        num = ''
                        while j >= 0 and sub[j].isdigit():
                            num = sub[j] + num
                            j -= 1
                        num = str(int(num) + 1)
                        next.append(sub[:j + 1] + num)
                        next.append(sub + word[i])
                    else:
                        next.append(sub + '1')
                        next.append(sub + word[i])
            ans = next

        return ans



Sol = Solution()
print Sol.generateAbbreviations('word')

