
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        words = []
        for word in s.split(' '):
            if word:
                words.append(word)

        return len(words[-1])
