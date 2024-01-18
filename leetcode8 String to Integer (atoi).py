class Solution:
    def myAtoi(self, s: str) -> int:
        if not s:
            return 0
        s = s.lstrip()
        if not s:
            return 0

        isPositive = s[0] != '-'
        if s[0] in '+-':
            s = s[1:]

        i = 0
        ans = []
        while i < len(s) and s[i].isdigit():
            ans.append(s[i])
            i += 1

        if not ans:
            return 0
        ans = int(''.join(ans))
        if not isPositive:
            ans = -ans
        if ans < -2147483648:
            return -2147483648
        elif ans > 2147483647:
            return 2147483647
        return ans


print(Solution().myAtoi('   -42'))
print(Solution().myAtoi('4193 with words'))
print(Solution().myAtoi('words and 987'))
print(Solution().myAtoi('-91283472332'))
