class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        lst = []

        for i in range(rowIndex+1):
            if i == 0 or i == rowIndex:
                lst.append(1)
            else:
                multiplier1 = 1
                multiplier2 = 1
                for j in range(i):
                    multiplier1 = multiplier1*(rowIndex-j)
                    multiplier2 = multiplier2*(j+1)
                lst.append(multiplier1/multiplier2)

        return lst

a = Solution()
b = a.getRow(8)
print b

