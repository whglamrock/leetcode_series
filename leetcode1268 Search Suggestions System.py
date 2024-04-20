from collections import defaultdict
from typing import List

class TrieNode:
    def __init__(self):
        self.words = []
        self.children = defaultdict(TrieNode)

# In real interview the interviewer is most likely more interested in the Trie solution. Note that we cannot use heapq
# to store the list of words and do heappop(words). The python somehow stupidly pops out a single char instead of a word.
class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        # important! this avoids using heapq
        products.sort()
        root = TrieNode()
        for product in products:
            curr = root
            for char in product:
                curr = curr.children[char]
                if len(curr.words) < 3:
                    curr.words.append(product)

        ans = []
        curr = root
        for i, char in enumerate(searchWord):
            if char not in curr.children:
                ans.append([])
                break
            curr = curr.children[char]
            ans.append(curr.words[:3])

        while i < len(searchWord) - 1:
            ans.append([])
            i += 1

        return ans


print(Solution().suggestedProducts(products=["mobile", "mouse", "moneypot", "monitor", "mousepad"], searchWord="mouse"))


'''
# naive hashmap solution, which actually runs faster in stupid leetcode. Interviewer may look for Trie solution
class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        prefixToWords = defaultdict(list)
        for word in products:
            for i in range(1, len(word) + 1):
                prefix = word[:i]
                prefixToWords[prefix].append(word)

        for prefix in prefixToWords:
            prefixToWords[prefix].sort()

        ans = []
        for i in range(1, len(searchWord) + 1):
            prefix = searchWord[:i]
            if prefix not in prefixToWords:
                ans.append([])
            else:
                ans.append(prefixToWords[prefix][:3])

        return ans
'''