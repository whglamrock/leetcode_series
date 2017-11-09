
from collections import deque

class Solution(object):
    def reverseStr(self, s, k):

        if not s:
            return ''

        buff = deque()
        ans = []
        for i, char in enumerate(s):
            if (i / k) % 2 == 0:
                buff.appendleft(char)
            else:
                buff.append(char)
            # remember it's i + 1
            if (i + 1) % k == 0:
                ans.extend(buff)
                buff = deque()

        ans.extend(buff)
        return ''.join(ans)



Sol = Solution()
s = 'abcdefgdsfwfqwd'
k = 3
print Sol.reverseStr(s, k)

