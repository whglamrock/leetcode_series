
''' (96ms solution)
class Solution(object):
    def intToRoman(self, num):

        M = ["", "M", "MM", "MMM"];
        C = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"];
        X = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"];
        I = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"];

        return M[num/1000] + C[(num%1000)/100] + X[(num%100)/10] + I[num%10];
'''

class Solution(object):
    def intToRoman(self, num):

        ans = ''
        if num/1000 != 0:
            for i in range(num/1000):
                ans += 'M'
            num -= int(num/1000) * 1000
        if num/900 != 0:
            ans += 'CM'
            num -= 900
        if num/500 != 0:
            ans += 'D'
            num -= 500
        if num/400 != 0:
            ans += 'CD'
            num -= 400
        if num/100 != 0:
            for i in range(num/100):
                ans += 'C'
            num -= int(num/100)* 100
        if num/90 != 0:
            ans += 'XC'
            num -= 90
        if num/50 != 0:
            ans += 'L'
            num -= 50
        if num/40 != 0:
            ans += 'XL'
            num -= 40
        if num/10 != 0:
            for i in range(num/10):
                ans += 'X'
            num -= int(num/10) * 10
        if num/9 != 0:
            ans += 'IX'
            num -= 9
        if num/5 != 0:
            ans += 'V'
            num -= 5
        if num/4 != 0:
            ans += 'IV'
            num -= 4
        if num/1 != 0:
            for i in range(num/1):
                ans += 'I'
            num -= int(num/1) * 10

        return ans












