
# There is no better solution than O(NlogN)

class Solution(object):
    def twoSumLessThanK(self, A, K):

        if len(A) == 1:
            return -1

        A.sort()
        candidate = -2147483648

        i, j = 0, len(A) - 1
        while i < j:
            tmp = A[i] + A[j]
            if tmp >= K:
                j -= 1
            else:
                candidate = max(candidate, tmp)
                # the case A[i + 1] + A[j] >= K will be examined in the next loop
                i += 1

        return -1 if candidate == -2147483648 else candidate

