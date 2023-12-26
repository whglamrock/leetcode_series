from typing import List


class Solution:
    def findRLEArray(self, encoded1: List[List[int]], encoded2: List[List[int]]) -> List[List[int]]:
        freq1, freq2 = 0, 0
        i, j = -1, -1
        m = len(encoded1)
        n = len(encoded2)
        ans = []

        while i < m and j < n:
            if freq1 == 0:
                i += 1
                if i == m:
                    break
                freq1 = encoded1[i][1]
            if freq2 == 0:
                j += 1
                if j == n:
                    break
                freq2 = encoded2[j][1]

            minOfFreq = min(freq1, freq2)
            prodNum = encoded1[i][0] * encoded2[j][0]
            if not ans or prodNum != ans[-1][0]:
                ans.append([prodNum, minOfFreq])
            else:
                ans[-1][1] += minOfFreq
            freq1 -= minOfFreq
            freq2 -= minOfFreq

        return ans


print(Solution().findRLEArray(encoded1=[[1, 3], [2, 1], [3, 2]], encoded2=[[2, 3], [3, 3]]))
