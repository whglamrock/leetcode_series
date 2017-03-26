
# O(N^2) time/space dp solution. Very hard.
# idea from: https://mp.weixin.qq.com/s?__biz=MzA5MzE4MjgyMw==&mid=2649455553&idx=1&sn=9e94d5c9d76d53b052a6c6dbafd5f040&chksm=887e15c9bf099cdfe22780affcd3246294fa47adf1bd66ac1da10fe886027ca0c2656bc7c29e&scene=1&srcid=0923iCjzi92RFnHVNR9lEnvw&key=1a6dc58b177dc626b434194d69d6b5f7912f8fa741667ae06cae7c3b077c330a258cf49566ddcb6053f64ecde9bac429&ascene=0&uin=MTM4NzI5NDIyMA%3D%3D&devicetype=iMac+MacBookPro12%2C1+OSX+OSX+10.10.5+build(14F1021)&version=11020201&pass_ticket=0Oc7O%2F49M13jDess06J2Ds5EZWACRTemBS9%2FhyZIaqAm96dnRQvMxzcAmFOIL1hO

class Solution(object):
    def minCut(self, s):

        if (not s):
            return 0

        n = len(s)
        matrix = [[0 for i in xrange(n)] for j in xrange(n)]
        for i in xrange(n):
            matrix[i][i] = 1

        dp = [-1]
        for i in xrange(n):
            dp.append(i)

        for i in xrange(1, n):
            for j in xrange(i):
                if s[i] == s[j] and (j == i - 1 or matrix[j + 1][i - 1] == 1):
                    dp[i+1] = min(dp[i + 1], dp[j] + 1)
                    matrix[j][i] = 1
            dp[i+1] = min(dp[i + 1], dp[i] + 1)

        #print dp
        #for item in matrix:
            #print(item)
        return dp[-1]



Sol = Solution()
s = 'aacaddqw'
print Sol.minCut(s)
