class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 0:
            return []
        if numRows == 1:
            return [[1]]
        if numRows == 2:
            return [[1],[1,1]]

        lst = [[]for k in range(numRows)]
        lst[0] = [1]
        lst[1] = [1,1]

        for i in range(2,numRows):
            lst[i].append(1)
            for j in range(i-1):
                lst[i].append(lst[i-1][j]+lst[i-1][j+1])
            lst[i].append(1)

        return lst

a = Solution()
b = a.generate(5)
print b




