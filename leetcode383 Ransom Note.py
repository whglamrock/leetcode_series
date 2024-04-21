from collections import Counter

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magazine = Counter(magazine)
        ransomNote = Counter(ransomNote)
        for char in ransomNote:
            if char not in magazine or ransomNote[char] > magazine[char]:
                return False

        return True
