class Solution(object):
    def getPermutation(self, n, k):

        jiecheng = 1
        for i in xrange(1,n+1):
            jiecheng *= i

        divider = n
        base = []
        used = set([])
        while divider > 0:
            interval = jiecheng/divider
            cur, counter = 0, 0
            while counter * interval < k:
                cur += 1
                counter += 1    # used to count the number of interval it's currently in
                while cur in used:  # in permutation sequence, every number(1~n) can only be used once
                    cur += 1
            base.append(str(cur))    # stores the number we've chosen
            used.update({cur})
            k -= (counter-1) * interval    # the k left over
            if k == 0:
                break
            jiecheng /= divider    # this two lines are designed to change the interval in next loop
            divider -= 1

        return ''.join(base)


Sol = Solution()
n = 4
k = 2
print Sol.getPermutation(n, k)