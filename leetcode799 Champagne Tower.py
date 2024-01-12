# we have to use dp because not all of cups in a row are filled full at the same time.
# this means when any cup in row i is full, it will start overflowing to row i + 1,
# even when not all cups at row i are full
class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        currRow = [poured]
        for i in range(query_row + 1):
            # the currRow has i + 1 cups, and nextRow has i + 2
            nextRow = [0] * (i + 2)
            # only loop through the currRow
            for j in range(i + 1):
                # if the champagne is overflowing
                if currRow[j] >= 1:
                    nextRow[j] += (currRow[j] - 1) / 2
                    nextRow[j + 1] += (currRow[j] - 1) / 2
                    currRow[j] = 1
            if i < query_row:
                currRow = nextRow

        return currRow[query_glass]


print(Solution().champagneTower(25, 6, 1))
