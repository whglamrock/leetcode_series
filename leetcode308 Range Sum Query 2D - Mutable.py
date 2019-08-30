
# Binary Index Tree solution will be more impressive in real interview
    # see how BIT is constructed in a clean way: https://www.hackerearth.com/zh/practice/data-structures/advanced-data-structures/fenwick-binary-indexed-trees/tutorial/

# update: O(logN); sumRegion: O(M * logN)

class NumMatrix(object):

    # leetcode does give bullshit corner case when matrix == [[]]
    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        self.matrix = matrix
        self.bits = []
        if matrix:
            for i in xrange(len(matrix)):
                # covers the corner case when matrix[i] is empty
                bit = self.buildBIT(matrix[i])
                self.bits.append(bit)

    def update(self, row, col, val):
        """
        :type row: int
        :type col: int
        :type val: int
        :rtype: None
        """
        diff = val - self.matrix[row][col]
        self.matrix[row][col] = val
        self.updateBIT(self.bits[row], col, diff)

    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        ans = 0
        for i in xrange(row1, row2 + 1):
            ans += self.queryBIT(self.bits[i], col2) - self.queryBIT(self.bits[i], col1 - 1)
        return ans

    def buildBIT(self, nums):
        n = len(nums)
        bit = [0 for _ in xrange(n + 1)]

        for i in xrange(n):
            j = i + 1
            while j <= n:
                bit[j] += nums[i]
                j += j & (-j)

        return bit

    # in bit the i should be i + 1
    def queryBIT(self, bit, i):
        # get the prefix sum
        i += 1
        prefixSum = 0
        while i > 0:
            prefixSum += bit[i]
            i -= i & (-i)

        return prefixSum

    # in bit the i should be i + 1
    def updateBIT(self, bit, i, diff):
        i += 1
        while i < len(bit):
            bit[i] += diff
            i += i & (-i)



matrix = [[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]]
Sol = NumMatrix(matrix)
Sol.update(1, 0, 1)
print Sol.sumRegion(2, 1, 4, 3)
Sol.update(3, 2, 2)
print Sol.sumRegion(2, 1, 4, 3)



'''
# O(n) solution for sum abd update function. Keep a accumulate sum matrix of each row

# do notice the shitty corner case given leetcode when matrix == [[]], although in real interview this 
    # probably won't occur (but do remember to ask the corner case). 

class NumMatrix(object):

    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        self.matrix = matrix
        self.m = len(matrix) if matrix else 0
        self.n = len(matrix[0]) if (matrix and matrix[0]) else 0
        
        self.rowSum = [[0 for j in xrange(self.n)] for i in xrange(self.m)]
        for i in xrange(self.m):
            for j in xrange(self.n):
                if j >= 1:
                    self.rowSum[i][j] += self.rowSum[i][j - 1] + matrix[i][j]
                else:
                    self.rowSum[i][j] = matrix[i][j]

    def update(self, row, col, val):
        """
        :type row: int
        :type col: int
        :type val: int
        :rtype: None
        """
        diff = val - self.matrix[row][col]
        self.matrix[row][col] = val
        for j in xrange(col, self.n):
            self.rowSum[row][j] += diff

    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        ans = 0
        for i in xrange(row1, row2 + 1):
            if col1 > 0:
                ans += self.rowSum[i][col2] - self.rowSum[i][col1 - 1]
            else:
                ans += self.rowSum[i][col2]
        
        return ans
'''
