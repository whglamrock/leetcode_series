
# Be careful about a very possible follow-up (seen in pinterest interview): https://leetcode.com/discuss/interview-question/algorithms/124839/pinterest-reverse-count-and-say
# to reverse countAndSay method. We need to ask about whether the interviewer wants a single digit reverse.
# e.g., 1211 could be 121 one's, or 1 two and 1 one.
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
