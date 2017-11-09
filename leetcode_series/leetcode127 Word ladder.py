
# the stupid leetcode changed the type of wordList from set to list.

class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):

        if not wordList:
            return 0    # according to the problem definition
        # it's told by the definition that beginWord != endWord

        wordList = set(wordList)
        # to record the current status of transformation
        todo = {beginWord}
        # we can discard the beginWord or not
        #wordList.discard(beginWord)
        length = 2

        while todo:
            new = set()
            for word in todo:
                for i in xrange(len(word)):
                    for char in 'abcdefghijklmnopqrstuvwxyz':
                        newword = word[:i] + char + word[i + 1:]
                        if newword in wordList:
                            wordList.discard(newword)
                            new.add(newword)
            if endWord in new:
                return length
            length += 1
            todo = new

        return 0    # the above BFS already tried out all possibilities



beginWord = "hit"
endWord = "hit"
wordList = {"hit", "hot","dot","dog","lot","log"}
Sol = Solution()
print Sol.ladderLength(beginWord, endWord, wordList)
