
# the hint is to devide num into triplets so we can deal with them one by one
# P.S., there is no need to add 'self.' before the LESSTHAN20, etc.

class Solution(object):
    def numberToWords(self, num):

        if num == None: return ''
        if num == 0: return 'Zero'

        # notice how each digit array is constructed. The goal is to use it conveniently
        LESSTHAN20 = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
        TENS = ["", "Ten", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
        THOUSANDS = ["", "Thousand", "Million", "Billion"]

        # just to remember that every return value of helper function has space at the end
        #   so there is no need to add space before 'Thousands[i]'
        def helper(triplet):

            # very necessary, to avoid add additional space if triplet == 0, try test case: num == 50688
            if triplet == 0:
                return ''
            elif triplet < 20:
                return LESSTHAN20[triplet] + ' '
            elif triplet < 100:
                return TENS[triplet / 10] + ' ' + helper(triplet % 10)
                # <=> return TENS[triplet / 10] + ' ' + (LESSTHAN20[triplet % 10] + ' ' if triplet % 10 > 0 else '')
            else:
                return LESSTHAN20[triplet / 100] + ' Hundred ' + helper(triplet % 100)

        i = 0
        ans = ''
        while num > 0:
            # notice when num == 1000000 and why the if statement is necessary
            if num % 1000 > 0:
                ans = helper(num % 1000) + THOUSANDS[i] + ' ' + ans
            num /= 1000
            i += 1

        return ans.rstrip(' ')



Sol = Solution()
num = 1234567890
print Sol.numberToWords(num)
