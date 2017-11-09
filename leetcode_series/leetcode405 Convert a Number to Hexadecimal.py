
class Solution(object):
    def toHex(self, num):

        if num == 0:
            return '0'

        mask = 0
        for i in xrange(32):
            mask |= 1 << i

        if num < 0:
            num = ((-num) ^ mask) + 1

        #print num
        ans = []
        while num > 0:
            ans.append(num % 16)
            num = (num - num % 16) / 16

        ans.reverse()
        additionaldigits = ['a', 'b', 'c', 'd', 'e', 'f']
        for i in xrange(len(ans)):
            if ans[i] >= 10:
                ans[i] = additionaldigits[ans[i] - 10]
            else:
                ans[i] = str(ans[i])

        return ''.join(ans)