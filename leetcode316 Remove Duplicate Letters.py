# Record the last occurrence (index) of each char. see: https://leetcode.com/problems/remove-duplicate-letters/solutions/1859515/python-o-n-beats-98-stack-detailed-explanation-simple/
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        charToLastIndex = {}
        for i, char in enumerate(s):
            charToLastIndex[char] = i

        stack = []
        visited = set()
        for i, char in enumerate(s):
            if char not in visited:
                while stack and stack[-1] > char and charToLastIndex[stack[-1]] > i:
                    visited.discard(stack.pop())
                visited.add(char)
                stack.append(char)

        return ''.join(stack)


print(Solution().removeDuplicateLetters(s="cbacdcbc"))
print(Solution().removeDuplicateLetters(s="bcabc"))
