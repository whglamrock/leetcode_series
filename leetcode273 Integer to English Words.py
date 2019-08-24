
# The most important tip to remember is divide the number into triplets and use recursion with the helper funciton

# Follow up question: https://leetcode.com/problems/integer-to-english-words/discuss/216295/Follow-up-on-this-question

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



'''
# for follow-up, need to rewrite the convertChunk function

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

        num = str(num)
        i = 0
        anspool = []
        while i < len(num):
            chunk = num[i:i + 3]
            anspool.append(self.convertChunk(chunk))
            i += 3

        ans = ''
        for i in range(len(anspool))[::-1]:
            if anspool[i]:
                ans = ans + anspool[i] + ' ' + self.THOUSANDS[i] + ' '

        return ans.rstrip(' ')

    # in this case the num is a string whose length is at most 3
    # e.g., 421
    def convertChunk(self, num):
        if int(num) == 0:
            return ''
        elif len(num) == 1:
            return self.LESSTHAN20[int(num)]
        elif len(num) == 2:
            reverseNum = num[::-1]
            if int(reverseNum) < 20:
                return self.LESSTHAN20[int(reverseNum)]
            else:
                return self.TENS[int(num[1])] + ' ' + self.convertChunk(num[0])
        # 3 digits
        else:
            if int(num[2]) > 0:
                return self.LESSTHAN20[int(num[2])] + ' Hundred ' + self.convertChunk(num[:2])
            else:
                return self.convertChunk(num[:2])


    def __init__(self):
        self.LESSTHAN20 = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Eleven",
                           "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
        self.TENS = ["", "Ten", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
        # since the num can be at most 2147483647
        self.THOUSANDS = ["", "Thousand", "Million", "Billion"]
        
'''