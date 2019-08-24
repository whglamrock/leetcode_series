
# The most important tip to remember is divide the number into triplets and use recursion with the helper funciton

class Solution(object):
    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == None:
            return ''
        if num == 0:
            return 'Zero'

        i = 0
        ans = ''
        while num:
            # very important! To filter out the '000's.
            if num % 1000 > 0:
                ans = self.convertChunk(num % 1000) + self.THOUSANDS[i] + ' ' + ans
            i += 1
            num /= 1000

        return ans.rstrip(' ')

    def convertChunk(self, num):
        if num == 0:
            return ''
        elif num < 20:
            return self.LESSTHAN20[num] + ' '
        elif num < 100:
            return self.TENS[num / 10] + ' ' + self.convertChunk(num % 10)
        else:
            return self.LESSTHAN20[num / 100] + ' Hundred ' + self.convertChunk(num % 100)

    def __init__(self):
        self.LESSTHAN20 = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Eleven",
                           "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
        self.TENS = ["", "Ten", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
        # since the num can be at most 2147483647
        self.THOUSANDS = ["", "Thousand", "Million", "Billion"]



print Solution().numberToWords(1234567891)
print Solution().numberToWords(1000000000)
print Solution().numberToWords(1000120101)
print Solution().numberToWords(10000)
