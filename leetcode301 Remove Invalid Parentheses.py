
from collections import deque

# In real interview, it's hard to remember the "reverse string" solution. So it's OK to give the following solution

class Solution(object):
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        if s == None:
            return []
        if s == '':
            return ['']

        queue = deque()
        queue.append(s)
        visited = set()
        ans = []

        while queue:
            string = queue.popleft()
            if self.isValid(string):
                # we only need to "remove minimum number of invalid parentheses"
                if not ans or (ans and len(ans[0]) == len(string)):
                    ans.append(string)
                continue

            # generate all possible combinations
            for i in xrange(len(string)):
                if string[i] not in '()':
                    continue
                newString = string[:i] + string[i + 1:]
                if newString not in visited:
                    queue.append(newString)
                    visited.add(newString)

        return ans

    def isValid(self, s):
        i, n = 0, len(s)
        count = 0
        while i < n:
            if s[i] not in '()':
                i += 1
                continue
            if s[i] == '(':
                count += 1
            elif s[i] == ')':
                count -= 1
            if count < 0:
                return False
            i += 1

        return count == 0



print Solution().removeInvalidParentheses("(a)()())")



# But to get strong hire, you would probably need to give out the solution or at least idea without using set to check,
    # see: https://leetcode.com/problems/remove-invalid-parentheses/discuss/75027/Easy-Short-Concise-and-Fast-Java-DFS-3-ms-solution
# notice why last_i and last_j are both used and what they are used for:
    # 1) last_i records the last valid position after removal, so in the next recursion, we can avoid
    # counting '(' and ')' from the start of the string;
    # 2) last_j records the last removal position, so the new removal position has to start from it
# For consecutive ')'s, ONLY remove the FIRST one
# E.g., using '()()()) ())' as example to run the solution in the above link to understand why we need both last_i & last_j are

# P.S. another important theory is: when the first extra ')' occurs, we can remove any of the previous ')' to make
    # the whole prefix valid










