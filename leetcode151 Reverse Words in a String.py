# the python split will simply ignore all spaces if without a specific splitter.
class Solution:
    def reverseWords(self, s: str) -> str:
        # no splitter needed, then the space will be simply skipped
        return ' '.join(s.split()[::-1])


Sol = Solution()
print(Sol.reverseWords('  suck  my  dick  '))
