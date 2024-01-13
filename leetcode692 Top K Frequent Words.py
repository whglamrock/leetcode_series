
from collections import Counter
from heapq import *

class Node:
    def __init__(self, count, word):
        self.count = count
        self.word = word

    def __cmp__(self, o):
        if self.count != o.count:
            return self.count > o.count
        else:
            return self.word < o.word


class Solution(object):
    def topKFrequent(self, words, k):

        wordCount = Counter(words)
        q = []
        for word in wordCount:
            count = wordCount[word]
            node = Node(count, word)
            heappush(q, node)
            while len(q) > k:
                heappop(q)

        ans = []
        while q:
            node = heappop(q)
            ans.append(node.word)

        return ans[::-1]


print(Solution().topKFrequent(["i", "love", "leetcode", "i", "love", "coding"], 1))


'''
# O(nlogn) solution

class Solution(object):
    def topKFrequent(self, words, k):

        wordCount = Counter(words)
        ret = sorted(wordCount, key=lambda word: (-wordCount[word], word))

        return ret[:k]
'''

