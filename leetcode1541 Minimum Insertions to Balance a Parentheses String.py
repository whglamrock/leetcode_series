
# first, add any missing ')' if there is any odd number of consecutive ')'s.
# Then replace each pair with a '}' and generate a modified s char array.
# At last, this problem becomes finding min operation to make a valid parenthesis
class Solution:
    def minInsertions(self, s: str) -> int:
        modifiedS = []
        minAdd = 0
        numOfConsecutiveBackParenthesis = 0
        for char in s:
            if char == '(':
                if numOfConsecutiveBackParenthesis == 1:
                    minAdd += 1
                    modifiedS.append('}')
                    numOfConsecutiveBackParenthesis = 0
                modifiedS.append('(')
            else:
                numOfConsecutiveBackParenthesis += 1
                if numOfConsecutiveBackParenthesis >= 2:
                    modifiedS.append('}')
                    numOfConsecutiveBackParenthesis -= 2

        if numOfConsecutiveBackParenthesis:
            modifiedS.append('}')
            minAdd += 1

        stack = []
        for char in modifiedS:
            if char == '(':
                stack.append(char)
            else:
                if stack and stack[-1] == '(':
                    stack.pop()
                    continue
                minAdd += 1

        # in case there are some '(' left in the stack
        if stack:
            minAdd += 2 * len(stack)

        return minAdd


print(Solution().minInsertions("(()))"))
print(Solution().minInsertions("())"))
print(Solution().minInsertions("))())("))
print(Solution().minInsertions("(()))(()))()())))"))
