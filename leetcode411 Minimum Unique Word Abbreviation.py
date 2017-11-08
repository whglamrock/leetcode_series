
# My ugly AC solution by directly borrowing the code from lc408 and lc320.
# Optimization could be done in:
# a) dynamically generate the abbrevtion of a given length using DFS and backtracking;
# b) use binary search to decide the length mentioned above so in general it's "better" than
#    checking the abbr of length from 1 to n.

# in real interview, the interviewer would probbaly let you solve the lc320 and lc408 first and
# let you do this question. In this case we just need to write the minAbbreviation and
# calculateLen function. However, the generateAbbr function might need to be optimized.

class Solution(object):

    def minAbbreviation(self, target, dictionary):

        count = 0
        for string in dictionary:
            if len(string) == len(target):
                count += 1
        if count == 0: return str(len(target))

        self.lendic = {}
        self.abbrevations = set(self.generateAbbr(target))
        self.calculateLen(target, self.abbrevations)
        n = len(target)

        for i in xrange(1, n + 1):
            for abbr in self.lendic[i]:
                flag = True
                for string in dictionary:
                    if len(string) != len(target): continue
                    if self.validWordAbbreviation(string, abbr):
                        flag = False
                        break
                if flag: return abbr

    # calculate the length of different abbrs and add it to lendic.
    def calculateLen(self, word, abbrevations):

        for abbr in abbrevations:
            numcount = 0
            charcount = 0

            for i, char in enumerate(abbr):
                if (char.isdigit() and i == 0) or (i > 0 and char.isdigit() and (not abbr[i - 1].isdigit())):
                    numcount += 1
                elif not char.isdigit():
                    charcount += 1

            length = charcount + numcount
            if length not in self.lendic:
                self.lendic[length] = set()
            self.lendic[length].add(abbr)

    def generateAbbr(self, word):

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

    def validWordAbbreviation(self, word, abbr):

        if (not abbr): return False

        i, j = 0, 0
        num = []
        while i < len(word) and j < len(abbr):
            #print i, j
            if word[i] == abbr[j]:
                i += 1
                j += 1
            else:
                if '0' <= abbr[j] <= '9':
                    while j < len(abbr) and '0' <= abbr[j] <= '9':
                        num.append(abbr[j])
                        j += 1
                    if num[0] == '0':
                        return False
                    num = ''.join(num)
                    proceed = int(num)
                    i += proceed
                    num = []
                else:
                    return False

        return i == len(word) and j == len(abbr)