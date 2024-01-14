from collections import defaultdict
from typing import List

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


print(Solution().suggestedProducts(products=["mobile", "mouse", "moneypot", "monitor", "mousepad"], searchWord="mouse"))
