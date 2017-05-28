
# O(n) time complexity, O(1) time space complexity

class Solution(object):
    def romanToInt(self, s):

        # there is no need to check whether s is empty because the definition said input will >= 1
        singleromantoint = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        n = len(s)
        if n == 1:
            return singleromantoint[s]

        i, ans = 0, 0
        while i < n - 1:
            currdigit, nextdigit = singleromantoint[s[i]], singleromantoint[s[i + 1]]
            if currdigit < nextdigit:
                ans += nextdigit - currdigit
                i += 2
            else:
                # can't directly do "ans += nextdigit + curdigit" because the
                #   nextdigit in this loop could be attached with the nextdigit
                #   in the next loop
                ans += currdigit
                i += 1
            if i == n - 1:  # it applies to both conditions
                ans += singleromantoint[s[i]]

        return ans



a = 'D'
Sol = Solution()
print Sol.romanToInt(a)






