
# note the problem definition and all the conditions

class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):

        if not wordList:
            return 0  # according to the problem definition
        # it's told by the definition that beginWord != endWord

        wordList = set(wordList)
        letters = "abcdefghijklmnopqrstuvwxyz"
        todo = {beginWord}

        length = 2
        while todo:
            next = set()
            for word in todo:
                for i in xrange(len(word)):
                    for char in letters:
                        newWord = word[:i] + char + word[i + 1:]
                        if newWord in wordList:
                            if newWord == endWord:
                                return length
                            next.add(newWord)
                            wordList.discard(newWord)  # this word is visited
            todo = next
            length += 1

        return 0 # the above BFS already tried out all possibilities



beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]
Sol = Solution()
print Sol.ladderLength(beginWord, endWord, wordList)
