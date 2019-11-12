
class Solution(object):
    def braceExpansionII(self, expression):
        """
        :type expression: str
        :rtype: List[str]
        """
        stack = []
        for c in expression:
            if c == '{':
                stack.append(c)
            elif c == ',':
                stack.append(c)
            # '}' always comes with ',' 2 chars before
            elif c == '}':
                while len(stack) >= 2 and stack[-2] == ',':
                    set2 = stack.pop()
                    stack.pop()  # pop the useless ','
                    stack[-1].update(set2)

                assert(stack[-2] == '{')
                # remove the '{'
                lastSet = stack.pop()
                stack[-1] = lastSet
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
        return sorted(stack[0])



print Solution().braceExpansionII('a{b,c}{d,e}f{g,h}')
print Solution().braceExpansionII('{a,b,c}')
print Solution().braceExpansionII('{a,b}{c,d}')
