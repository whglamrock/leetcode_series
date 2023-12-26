
class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:

        stack = []
        for i, char in enumerate(s):
            if stack and char == stack[-1][0]:
                stack[-1][1] += 1
            else:
                stack.append([char, 1])
            if stack[-1][1] == k:
                stack.pop()

        ans = []
        for item in stack:
            for i in range(item[1]):
                ans.append(item[0])
        return ''.join(ans)


print(Solution().removeDuplicates(s="deeedbbcccbdaa", k=3))
print(Solution().removeDuplicates(s="abcd", k=2))
print(Solution().removeDuplicates(s="pbbcggttciiippooaais", k=2))
