
# O(N) solution
# lstrip will strip all '0's on the left
# The idea is:
# e.g., k = 4. n = len(num)
# step 1: find the smallest digit from num[: n - 4], mark the index s1;
# step 2: find the smallest digit from num[s1 + 1: n - 3], mark the index s2;
# step 3: ...so on and so forth

# if at the end, the k still > 0, for case like num = '1222222', k = 3, we join
# out[:-k], otherwise join the complete out list.

class Solution(object):
    def removeKdigits(self, num, k):

        out = []
        for d in num:
            while k and out and out[-1] > d:
                out.pop()
                k -= 1  # every k -= 1 means we remove one digit
            out.append(d)

        if k:
            ans = ''.join(out[:-k]).lstrip('0')
        else:
            ans = ''.join(out).lstrip('0')
        if ans != '':
            return ans
        else:
            return '0'