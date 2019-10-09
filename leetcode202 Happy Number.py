
# this isn't really an easy level question.
    # 1) we need to do quite amount of calculation to find out the unhappySet cycle;
    # 2) we need to explain that the newly calculated number is getting smaller and smaller;
    # 3) once the number becomes 2 digit, it will either go into the unhappy cycle or finally get to 1

class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        unhappySet = {89, 145, 42, 20, 4, 16, 37, 58, 89}
        while n != 1:
            n = self.calculateNext(n)
            if n in unhappySet:
                return False

        return True

    def calculateNext(self, n):
        digits = []
        for digit in str(n):
            digits.append(int(digit) * int(digit))
        return sum(digits)



print Solution().isHappy(19)
print Solution().isHappy(8821242)

