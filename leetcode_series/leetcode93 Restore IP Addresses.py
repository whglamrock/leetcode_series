
# my own backtracking solution

class Solution(object):
    def restoreIpAddresses(self, s):

        todo = [(0, [])]
        ans = []
        while todo:
            next = []
            for i, prev in todo:
                if len(prev) == 4:  # when IP is formed
                    if i < len(s):  # if i is not the last char of s, we dumb this from our final ans.
                        continue
                    else:
                        ans.append(prev)
                if i < len(s) and s[i] == '0':  # no need to check whether s[i+1], s[i+2] are 0s,
                    # because '00' is not allowed in IP (e.g., 0.0.0.11 is legal, but 0.00.1.1 is not).
                    next.append((i+1, prev+['0']))
                else:   # if s[i] != 0, need to check s[i], s[i+1], s[i+2]
                    for j in xrange(i, i+3):
                        if j < len(s) and int(s[i:j+1]) < 256:
                            next.append((j+1, prev+[s[i:j+1]]))
            todo = next

        res = []
        while ans:
            res.append('.'.join(ans.pop()))

        return res