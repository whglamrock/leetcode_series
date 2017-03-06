class Solution(object):
    def wordsTyping(self, sentence, rows, cols):

        sentence = map(len, sentence)   # convert the string itself to its length
        if any(x > cols for x in sentence):
            return 0

        # current_row, current_col, current_word_in_sentence
        r, c, s = 1, 0, 0
        res = 0
        # store the repeat pattern
        pattern = {}

        while r <= rows:
            if sentence[s] > cols - c:
                # cannot fit
                r += 1
                c = 0
            if c == 0:
                if s not in pattern:
                    # store the pattern
                    pattern[s] = r, res
                else:
                    # repeat pattern found. Jump to the end
                    last_row, rounds = pattern[s]
                    res += (res - rounds) * ((rows - r + 1) / (r - last_row))
                    # (rows - r + 1) / (r -last_row) indicates how many times the pattern will repeat.
                    # notice that the '/' retrieves the bottom value of the division (5/2 -> 2)
                    r += ((rows - r + 1) / (r - last_row)) * (r - last_row)
            # Fill word
            c += (sentence[s]+1)
            s += 1
            # Last word in sentence met. Increment res if valid
            if s == len(sentence) and r <= rows:
                s = 0
                res += 1

        return res

Sol = Solution()
sentence = ['I', 'have', 'an', 'apple']
print Sol.wordsTyping(sentence, 4, 10)
