'''
Write doen the binary numbers of grade code in order when n == 4, all newly added numbers are based on previous level (add a '1'
or '0' to the end of each previous level number)
'''
class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        if n == 0:
            return [0]
        if n == 1:
            return [0,1]
        if n == 2:
            return [0,1,3,2]

        base = [3,2]
        res = [0,1,3,2]
        switch = 0
        for i in xrange(2,n):
            new = []
            for item in base:
                if switch%2 == 0:
                    new.append(item*2)
                    new.append(item*2+1)
                    res.append(item*2)
                    res.append(item*2+1)
                else:
                    new.append(item*2+1)
                    new.append(item*2)
                    res.append(item*2+1)
                    res.append(item*2)
                switch += 1
            base = new

        return res