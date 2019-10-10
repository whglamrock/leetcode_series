
class Solution(object):
    def letterCombinations(self, digits):

        if not digits: return []

        mapping = {'2': ['a', 'b', 'c'], '3': ['d', 'e', 'f'], '4': ['g', 'h', 'i'], '5': ['j', 'k', 'l'], '6': ['m', 'n', 'o'], '7': ['p', 'q', 'r', 's'], '8': ['t', 'u', 'v'], '9': ['w', 'x', 'y', 'z']}

        curr = ['']
        for digit in digits:
            next = []
            for item in curr:
                for letter in mapping[digit]:
                    next.append(item + letter)
            curr = next

        return curr



print Solution().letterCombinations('237')













