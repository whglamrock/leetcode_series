from typing import List

class Solution:
    def differByOne(self, dict: List[str]) -> bool:
        for i in range(len(dict[0])):
            generatedWords = set()
            for word in dict:
                generatedWord = word[:i] + '*' + word[i + 1:]
                if generatedWord in generatedWords:
                    return True
                generatedWords.add(generatedWord)

        return False
