
# boring question
class Solution:
    def countVowelPermutation(self, n: int) -> int:
        dpA, dpE, dpI, dpO, dpU = [0] * n, [0] * n, [0] * n, [0] * n, [0] * n
        dpA[0], dpE[0], dpI[0], dpO[0], dpU[0] = 1, 1, 1, 1, 1
        for i in range(1, n):
            # Each vowel 'a' may only be followed by an 'e'
            dpE[i] += dpA[i - 1]
            # Each vowel 'e' may only be followed by an 'a' or an 'i'
            dpA[i] += dpE[i - 1]
            dpI[i] += dpE[i - 1]
            # Each vowel 'i' may not be followed by another 'i'
            dpA[i] += dpI[i - 1]
            dpE[i] += dpI[i - 1]
            dpO[i] += dpI[i - 1]
            dpU[i] += dpI[i - 1]
            # Each vowel 'o' may only be followed by an 'i' or a 'u'
            dpU[i] += dpO[i - 1]
            dpI[i] += dpO[i - 1]
            # Each vowel 'u' may only be followed by an 'a'
            dpA[i] += dpU[i - 1]

        return (dpA[-1] + dpE[-1] + dpI[-1] + dpO[-1] + dpU[-1]) % (10 ** 9 + 7)
