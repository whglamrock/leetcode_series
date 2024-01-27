from collections import Counter, defaultdict
from typing import List, Dict

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        permutationLen = len(words) * len(words[0])
        ans = []
        wordCount = Counter(words)
        for i in range(len(s) - permutationLen + 1):
            substr = s[i:i + permutationLen]
            wordCountOfSubstr = self.getWordCountOfSubstring(substr, len(words[0]))
            if wordCountOfSubstr == wordCount:
                ans.append(i)
        return ans

    def getWordCountOfSubstring(self, substr: str, k: int) -> Dict[str, int]:
        wordCount = defaultdict(int)
        for i in range(0, len(substr) - k + 1, k):
            wordCount[substr[i:i + k]] += 1
        return wordCount


print(Solution().findSubstring(s='foobarbarfoothefoobarfooman', words=["foo", "bar", 'foo']))
