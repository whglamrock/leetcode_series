
# note the problem definition and all the conditions

class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):

        if not wordList:
            return 0  # according to the problem definition

        wordList = set(wordList)
        letters = "abcdefghijklmnopqrstuvwxyz"
        curr = {beginWord}

        length = 2
        while curr:
            next = set()
            for word in curr:
                for i in xrange(len(word)):
                    for char in letters:
                        newWord = word[:i] + char + word[i + 1:]
                        if newWord in wordList:
                            if newWord == endWord:
                                return length
                            next.add(newWord)
                            wordList.discard(newWord)  # this word is visited
            curr = next
            length += 1

        return 0



print Solution().ladderLength("hit", "cog", ["hot","dot","dog","lot","log","cog"])
