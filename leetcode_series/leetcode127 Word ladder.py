
class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):

        front, back = {beginWord}, {endWord}
        length = 2
        wordList.discard(beginWord)  # when beginWord == endWord and wordList contains beginWord,
        # it will return 2 if without this line. However, leetcode accepted without this line probabaly
        # cuz they don't have this extreme case.

        while front:
            # generate all valid transformations for the next loop
            new = set([])
            for word in front:
                for i in xrange(len(beginWord)):
                    for ch in "abcdefghijklmnopqrstuvwxyz":
                        new.update({word[:i]+ch+word[i+1:]})
            front = new & wordList    # "&" select the elements that in both set new and wordList

            if front & back:    # there are common elements, done
                return length
            length += 1

            if len(front) > len(back):    # reduce the size of front in next loop
                front, back = back, front
            wordList -= front    # (P.S.: "-=" works for set), dumb used transformations to avoid cycle

        return 0    # for case when beginWord == endWord



beginWord = "hit"
endWord = "hit"
wordList = {"hit", "hot","dot","dog","lot","log"}
Sol = Solution()
print Sol.ladderLength(beginWord, endWord, wordList)
