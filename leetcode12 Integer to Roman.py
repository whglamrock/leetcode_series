"""
# (96ms solution)
class Solution(object):
    def intToRoman(self, num):

        M = ["", "M", "MM", "MMM"];
        C = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"];
        X = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"];
        I = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"];

        return M[num/1000] + C[(num%1000)/100] + X[(num%100)/10] + I[num%10];
"""


# there are only going to be 4 digits
class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """

        thousands = num // 1000
        num = num % 1000

        hundreds = num // 100
        num = num % 100

        tens = num // 10
        num = num % 10

        singles = num

        ans = []
        # deal with thousands
        if thousands > 0:
            for i in range(thousands):
                ans.append('M')

        # deal with hundreds:
        if hundreds == 9:
            ans.append('CM')
        elif hundreds >= 5:
            ans.append('D')
            hundreds -= 5
            for i in range(hundreds):
                ans.append('C')
        elif hundreds == 4:
            ans.append('CD')
        else:
            for i in range(hundreds):
                ans.append('C')

        # deal with tens:
        if tens == 9:
            ans.append('XC')
        elif tens >= 5:
            ans.append('L')
            tens -= 5
            for i in range(tens):
                ans.append('X')
        elif tens == 4:
            ans.append('XL')
        else:
            for i in range(tens):
                ans.append('X')

        # deal with singles
        if singles == 9:
            ans.append('IX')
        elif singles >= 5:
            ans.append('V')
            singles -= 5
            for i in range(singles):
                ans.append('I')
        elif singles == 4:
            ans.append('IV')
        else:
            for i in range(singles):
                ans.append('I')

        return ''.join(ans)
