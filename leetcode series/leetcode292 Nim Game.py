# when I start with 4, I lose; when I start with 5,6,7, I can let my opponent start with 4, so I win;
# Repeat this loop by yourself starting with 8,9,10,11,...., you can find out if you start with 4k(k is positive
# integers), you lose.

class Solution(object):
    def canWinNim(self, n):

        return n%4 != 0

# no need to test
