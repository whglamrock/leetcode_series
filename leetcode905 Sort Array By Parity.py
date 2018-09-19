
# or use deque

class Solution(object):
    def sortArrayByParity(self, A):

        res = []
        for num in A:
            if num % 2 == 0:
                res.append(num)
        for num in A:
            if num % 2 != 0:
                res.append(num)

        return res
