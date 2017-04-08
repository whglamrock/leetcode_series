
# for more info about the read4 API, refer to lc157

from collections import deque

class Solution(object):
    def __init__(self):

        self.queue = deque()

    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Maximum number of characters to read (int)
        :rtype: The number of characters read (int)
        """

        index = 0
        while True:

            cnm = [''] * 4
            l = read4(cnm)
            self.queue.extend(cnm)

            curlen = min(len(self.queue), n - index)
            for i in xrange(curlen):
                buf[index] = self.queue.popleft()
                index += 1

            if curlen == 0: break

        return index