
# it should've been an easy question

class Solution(object):
    def complexNumberMultiply(self, a, b):

        def getcomplexnumber(string):

            j = 0
            res = []
            while j < len(string) and string[j] != '+':
                j += 1
            res.append(int(string[:j]))
            j += 1
            if j == '-':
                res.append(-int(string[j + 1:len(string) - 1]))
            else:
                res.append(int(string[j:len(string) - 1]))

            return res

        a = getcomplexnumber(a)
        b = getcomplexnumber(b)
        newa = a[0] * b[0] - a[1] * b[1]
        newb = a[0] * b[1] + a[1] * b[0]

        return str(newa) + '+' + str(newb) + 'i'

