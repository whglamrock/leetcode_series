
# idea coming from lc1096

class Solution(object):
    def expand(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        stack = []
        for c in S:
            if c == '{':
                stack.append(c)
            elif c == '}':
                # union all the previously computed char sets
                while stack and stack[-2] == ',':
                    set2 = stack.pop()
                    stack.pop() # pop the ','
                    stack[-1].update(set2)

                assert(stack[-2] == '{')
                # remove the stand alone '{'
                lastSet = stack.pop()
                stack[-1] = lastSet
            elif c == ',':
                stack.append(c)
            else:
                stack.append(set(c))
            while len(stack) >= 2 and type(stack[-1]) == set and type(stack[-2]) == set:
                set2 = stack.pop()
                set1 = stack.pop()
                newSet = set()
                for w1 in set1:
                    for w2 in set2:
                        newSet.add(w1 + w2)
                stack.append(newSet)

        assert(len(stack) == 1)
        return sorted(stack[-1])



print Solution().expand('{a,b}c{d,e}f')
print Solution().expand('abcd')
print Solution().expand('a{b,c}d')
