
# the problem description appeared to be super vague.
# need to ask more questions in real interview.

class Solution(object):
    def validUtf8(self, data):

        bitcount = 0

        for n in data:
            if n >= 192:
                if bitcount != 0:
                    return False
                if n >= 240:
                    bitcount = 3
                elif n >= 224:
                    bitcount = 2
                else:
                    bitcount = 1
            elif n >= 128:
                bitcount -= 1
                if (bitcount) < 0:
                    return False
            elif bitcount > 0:
                return False

        return bitcount == 0