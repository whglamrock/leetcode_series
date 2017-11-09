
# use part of the code from leetcode190 reverse bits

class Solution(object):
    
    def hammingWeight(self, n):
        def find(num):
            i = 0
            while 2**i<=num:
                i += 1
            i -= 1
            return i

        lst = []
        while n > 0:
            j = find(n)
            lst.append(j)
            n -= 2**j

        return len(lst)




