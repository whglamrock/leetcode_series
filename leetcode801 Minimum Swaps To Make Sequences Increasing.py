
class Solution(object):
    def minSwap(self, A, B):

        # min number of swaps if we fix or swap at position i
        fixRecord, swapRecord = 0, 1
        n = len(A)

        for i in xrange(1, n):
            prevFixRecord, prevSwapRecord = fixRecord, swapRecord
            if A[i] > A[i - 1] and B[i] > B[i - 1]:
                if A[i] > B[i - 1] and B[i] > A[i - 1]:  # it means we have the freedom to swap or not
                    fixRecord = min(prevFixRecord, prevSwapRecord)
                    swapRecord = min(prevFixRecord, prevSwapRecord) + 1
                else:  # we either fix record or swap the record under the precondition that the previous one is also swapped
                    fixRecord = prevFixRecord
                    swapRecord = prevSwapRecord + 1
            else:  # in this case, either swap this pair, or the previous pair has to be swapped
                fixRecord = prevSwapRecord
                swapRecord = prevFixRecord + 1

        return min(fixRecord, swapRecord)
