class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return '1'
        if n == 2:
            return '11'

        curr = '11'
        for i in range(n - 2):
            count = 0
            nextStr = []
            for j, char in enumerate(curr):
                count += 1
                if j + 1 >= len(curr) or curr[j + 1] != char:
                    nextStr.append(str(count) + char)
                    count = 0
            curr = ''.join(nextStr)

        return curr


print(Solution().countAndSay(9))








