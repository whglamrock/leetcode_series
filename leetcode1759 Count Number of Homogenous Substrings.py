class Solution:
    def countHomogenous(self, s: str) -> int:
        mod = 10 ** 9 + 7
        ans = 0
        curr = None
        currCount = 0
        for i, char in enumerate(s):
            if char != curr:
                curr = char
                currCount = 1
            else:
                currCount += 1
            if i == len(s) - 1 or s[i + 1] != char:
                ans += (currCount + 1) * currCount // 2
                ans %= mod

        return ans


print(Solution().countHomogenous(s="abbcccaa"))
print(Solution().countHomogenous(s="xy"))
print(Solution().countHomogenous(s="zzzzz"))
