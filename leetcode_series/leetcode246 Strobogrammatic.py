class Solution(object):
    def isStrobogrammatic(self, num):

        for i in xrange(len(num)/2+1):
            if num[i] == num[len(num)-i-1]:
                if num[i] != '0' and num[i] != '8' and num[i] != '1':
                    return False
            else:
                if set([num[i],num[len(num)-i-1]]) != set(['6','9']):
                    return False

        return True


Sol = Solution()
print Sol.isStrobogrammatic('69')