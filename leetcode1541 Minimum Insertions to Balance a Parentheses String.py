
# first, add any missing ')' if there is any odd number of consecutive ')'s.
# Then replace each pair with a '}' and generate a modified s char array.
# At last, this problem becomes finding min operation to make a valid parenthesis
class Solution:
    def minInsertions(self, s: str) -> int:
        consecutiveBackParenthesis = 0
        modifiedS = []
        minAdd = 0
        for char in s:
            if char == '(':
                if consecutiveBackParenthesis % 2 != 0:
                    modifiedS.append('}')
                    minAdd += 1
                    consecutiveBackParenthesis = 0
                modifiedS.append(char)
            else:
                consecutiveBackParenthesis += 1
                if consecutiveBackParenthesis % 2 == 0:
                    modifiedS.append('}')

        if consecutiveBackParenthesis % 2 != 0:
            modifiedS.append('}')
            minAdd += 1

        stack = []
        i = 0
        while i < len(modifiedS):
            if modifiedS[i] == '(':
                stack.append(modifiedS[i])
            else:
                if stack and stack[-1] == '(':
                    stack.pop()
                else:
                    minAdd += 1
            i += 1

        # this means there are some open parenthesis, '(', left in the stack
        if stack:
            minAdd += 2 * len(stack)

        return minAdd


print(Solution().minInsertions("(()))"))
print(Solution().minInsertions("())"))
print(Solution().minInsertions("))())("))
print(Solution().minInsertions("(()))(()))()())))"))
