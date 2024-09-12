from collections import Counter
from heapq import *
from typing import List


# for customized sort in heapq, we will have to write an class and overrides the __lt__ method
class Node:
    def __init__(self, count: int, word: str):
        self.count = count
        self.word = word

    def __lt__(self, other: 'Node'):
        if self.count != other.count:
            return self.count < other.count
        else:
            return self.word > other.word


class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
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