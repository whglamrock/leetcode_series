from math import ceil

# 1) For all '[]' pairs, we can simply remove them since they are already balanced
# 2) After removing them, you are left with stings like ']]][[[' and we need to make them balanced
# 3) Most greedily, you would wanna use one swap to make 2 balanced pairs (e.g., swap the 2nd and 2nd last in the above)
# 4) This left you with the ceiling((len(leftOverString) // 2 ) / 2)
class Solution:
    def minSwaps(self, s: str) -> int:
        stack = []
        for char in s:
            if char == ']' and stack and stack[-1] == '[':
                stack.pop()
                continue
            stack.append(char)

        return ceil((len(stack) // 2) / 2)
