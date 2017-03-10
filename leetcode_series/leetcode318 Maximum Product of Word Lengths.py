class Solution(object):
    def maxProduct(self, words):

        if not words:
            return 0
        curr_max = 0
        while words:
            curr_word = set(words[0])
            curr_len = len(words[0])
            words = words[1:]
            for word in words:
                #easy = set(word)   #the easy is not built with extra memory!
                for char in curr_word:
                    if char in word: #if char in easy: (p.s. this is very time consuming, cuz
                        # it equals to 'if char in set(word)'
                        break
                else:   # when the above for loop doesn't break, equals to 'char not in word', but much
                    # more efficient, cuz don't need to check the 'char' in 'word'
                    curr_max = max(curr_max, curr_len*len(word))

        return curr_max


Sol = Solution()
words = ["abcw", "baz", "foo", "bar", "xtfn", "abcdef"]
print Sol.maxProduct(words)

