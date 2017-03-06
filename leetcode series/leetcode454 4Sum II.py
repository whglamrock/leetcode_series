class Solution(object):
    def fourSumCount(self, A, B, C, D):

        dicab, diccd = {}, {}
        for a in A:
            for b in B:
                sumab = a + b
                if sumab not in dicab:
                    dicab[sumab] = 0
                dicab[sumab] += 1

        for c in C:
            for d in D:
                sumcd = c + d
                if sumcd not in diccd:
                    diccd[sumcd] = 0
                diccd[sumcd] += 1

        ans = 0
        for sumab in dicab:
            if -sumab in diccd:
                ans += dicab[sumab] * diccd[-sumab]

        return ans