
# the question says "You must not use any built-in BigInteger library or convert the inputs to integer directly"
  # so we need to use the ord() function which gets the ascii number

class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        int1 = 0
        for char in num1:
            int1 = int1 * 10 + ord(char) - ord('0')

        int2 = 0
        for char in num2:
            int2 = int2 * 10 + ord(char) - ord('0')

        return str(int1 + int2)