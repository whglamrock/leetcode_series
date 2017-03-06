# there is no way to do with better time complexity than the following and the space complexity is unchangable
class Solution(object):
    def findStrobogrammatic(self, n):

        if n == 0: return []
        if n == 1: return ['1', '0', '8']

        if n % 2 == 0:
            todo = {''}
        else:
            todo = {'1', '0', '8'}

        for i in xrange(n/2):
            next = set()
            for item in todo:
                next.add('0' + item + '0')
                next.add('1' + item + '1')
                next.add('8' + item + '8')
                next.add('6' + item + '9')
                next.add('9' + item + '6')
            todo = next

        res = []
        for item in todo:
            if not item.startswith('0'):
                res.append(item)

        return res

Sol = Solution()
print Sol.findStrobogrammatic(5)
