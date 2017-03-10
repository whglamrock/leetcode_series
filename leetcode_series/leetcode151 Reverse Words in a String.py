
# Solution with the 'split' trick: the python split will simply ignore all spaces
#   if without a specific splitter.

class Solution(object):
    def reverseWords(self, s):

        # no splitter needed, then the space will be simply skipped
        return ' '.join(s.split()[::-1])



Sol = Solution()
print Sol.reverseWords('  fk  you  again  ')


