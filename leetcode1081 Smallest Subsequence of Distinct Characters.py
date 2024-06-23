
# same as lc316. See intuition from: https://leetcode.com/problems/smallest-subsequence-of-distinct-characters/solutions/308210/java-c-python-stack-solution-o-n/
class Solution:
    def smallestSubsequence(self, s: str) -> str:
        charToLastIndex = {}
        for i, char in enumerate(s):
            charToLastIndex[char] = i

        stack = []
        for i, char in enumerate(s):
            # this makes sure len(stack) <= 26
            if char in stack:
                continue

            while stack and stack[-1] > char and charToLastIndex[stack[-1]] > i:
                stack.pop()
            stack.append(char)

        return ''.join(stack)
