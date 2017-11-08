
# The key is to avoid duplicates without using hashset.

class Solution(object):
    def removeInvalidParentheses(self, s):

        self.ans = []
        self.remove(s, 0, 0, ['(', ')'])
        return self.ans

    # on the left of lasti (excluding lasti) are valid parentheses
    def remove(self, s, lasti, lastj, par):

        count = 0
        # P.S., the start index of i is lasti, not lasti + 1
        for i in xrange(lasti, len(s)):

            if s[i] == par[0]:
                count += 1
            elif s[i] == par[1]:
                count -= 1
            if count >= 0: continue

            # j can be i, because s[i] also needs to be removed
            for j in xrange(lastj, i + 1):
                # only need to remove one parentheses from consecutive ones
                if s[j] == par[1] and (j == lastj or s[j] != s[j - 1]):
                    # after removing one char from s, the new 's' and s[i] will become valid again
                    self.remove(s[:j] + s[j + 1:], i, j, par)

            # no need to keep this recursion running
            return

        # at this point, no invalid s[i] is found in this direction
        reverseds = s[::-1]

        # this recursion is from left to right
        if par[0] == '(':
            self.remove(reverseds, 0, 0, [')', '('])
        # this recursion is from "right to left" (i.e., scan the reversestring from left to right),
        #   and we scan the string in both direction, so it's valid
        else:
            self.ans.append(reverseds)



Sol = Solution()
s = "(a)()())"
print Sol.removeInvalidParentheses(s)











