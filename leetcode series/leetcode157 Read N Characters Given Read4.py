# read the code, if really encountering this fucking problem, ask ton of questions!
# the number of chars in file could be less than, equal to, more than n
# the read4 API will record which point of file the last read4 function moved to

class Solution(object):
    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Maximum number of characters to read (int)
        :rtype: The number of characters read (int)
        """

        idx = 0
        while n > 0:

            # read file to cnm
            cnm = [''] * 4
            # l will be within 4, and cnm will be filled(i.e., changed) after calling read4
            # e.g., if l == 0, the cnm list will be empty
            l = read4(cnm)

            # if no more char in file, return
            if not l:
                return idx

            # write cnm into buf directly; i will be within 4
            for i in xrange(min(l, n)):
                # the following step won't cause index out of range, because the
                # the length of buf should be a very big number
                buf[idx] = cnm[i]   # this step is necessary
                idx += 1
                n -= 1

        return idx


# The whole question is really confusing and ridiculous.
