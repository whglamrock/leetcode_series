from collections import Counter

# O(N) no sort solution
class Solution:
    def reorganizeString(self, s: str) -> str:
        charCount = Counter(s)
        maxCount = 0
        mostFrequentChar = ''
        for char in charCount:
            if charCount[char] > maxCount:
                maxCount = charCount[char]
                mostFrequentChar = char

        n = len(s)
        if (n % 2 == 0 and maxCount > n // 2) or (n % 2 != 0 and maxCount > n // 2 + 1):
            return ''

        ans = [''] * n
        i = 0
        # fill the most frequent chars first
        while charCount[mostFrequentChar] > 0:
            ans[i] = mostFrequentChar
            charCount[mostFrequentChar] -= 1
            i += 2
        del charCount[mostFrequentChar]

        for char in charCount:
            while charCount[char] > 0:
                if i >= n:
                    i = 1
                ans[i] = char
                charCount[char] -= 1
                i += 2

        return ''.join(ans)


print(Solution().reorganizeString("aaasaaaaaaabxuhsdajkdsfdofs"))
print(Solution().reorganizeString("aaab"))
print(Solution().reorganizeString("aabc"))


# original O(N * log(N)) priority queue solution
'''
from heapq import *

class Solution:
    def reorganizeString(self, s: str) -> str:
        charCount = Counter(s)
        pq = []
        for char in charCount:
            heappush(pq, [-charCount[char], char])

        maxCount = -pq[0][0]
        if len(s) % 2 == 0 and maxCount > len(s) // 2:
            return ''
        if len(s) % 2 != 0 and maxCount > len(s) // 2 + 1:
            return ''

        ans = []
        while pq:
            count, char = heappop(pq)
            count = -count
            if ans and ans[-1] == char:
                if not pq:
                    return ''
                count2, secondMostFrequentChar = heappop(pq)
                count2 = -count2
                ans.append(secondMostFrequentChar)
                count2 -= 1
                if count2 > 0:
                    heappush(pq, [-count2, secondMostFrequentChar])
                heappush(pq, [-count, char])
            else:
                ans.append(char)
                count -= 1
                if count > 0:
                    heappush(pq, [-count, char])

        return ''.join(ans)
'''