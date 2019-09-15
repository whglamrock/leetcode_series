
from collections import defaultdict

class Solution(object):
    def longestWord(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        if not words:
            return

        lengthToWord = defaultdict(set)
        for word in words:
            lengthToWord[len(word)].add(word)

        length = 1
        curr = {''}
        ans = ''

        while length in lengthToWord:
            next = set()
            # use a lexicographically smallest string to avoid sorting
            currAns = ''

            for word in curr:
                for char in 'abcdefghijklmnopqrstuvwxyz':
                    newWord = word + char
                    if newWord in lengthToWord[length]:
                        next.add(newWord)
                        if not currAns or newWord < currAns:
                            currAns = newWord

            if next:
                curr = next
                ans = currAns
            # it's very important to remember to break here
            else:
                break

            length += 1

        return ans



print Solution().longestWord(["w","wo","wor","worl", "world"])
print Solution().longestWord(["a", "banana", "app", "appl", "ap", "apply", "apple"])


