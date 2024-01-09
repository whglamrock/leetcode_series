from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        digitToLetters = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        todo = ['']
        for digit in digits:
            nextTodo = []
            mappedChars = digitToLetters[digit]
            for char in mappedChars:
                for subStr in todo:
                    nextTodo.append(subStr + char)
            todo = nextTodo

        return todo


print(Solution().letterCombinations('237'))













