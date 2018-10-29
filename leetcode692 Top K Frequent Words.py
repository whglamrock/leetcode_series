
from heapq import *
from collections import Counter, defaultdict

class Node:
    def __init__(self, count, word):
        self.count = count
        self.word = word

    def __cmp__(self, o):
        if self.count != o.count:
            return self.count > o.count
        else:
            return self.word < o.word


# O(nlogk) solution

class Solution(object):
    def topKFrequent(self, words, k):

        q = []
        wordCount = Counter(words)
        for word in wordCount:
            count = wordCount[word]
            node = Node(count, word)
            heappush(q, node)
            if len(q) > k:
                heappop(q)

        intermediate = defaultdict(list)
        while q:
            # will always pop the smallest count and biggest word
            node = heappop(q)
            count, word = node.count, node.word
            intermediate[count].append(word)

        res = []
        for count in sorted(intermediate.keys())[::-1]:
            # the word is added in reverse alphabetic order when count is same
            res += intermediate[count][::-1]

        return res



Sol = Solution()
print Sol.topKFrequent(["i", "love", "leetcode", "i", "love", "coding"], 1)



'''
# O(nlogn) solution

class Solution(object):
    def topKFrequent(self, words, k):

        wordCount = Counter(words)
        ret = sorted(wordCount, key=lambda word: (-wordCount[word], word))

        return ret[:k]
'''

