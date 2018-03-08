
class Solution(object):
    def letterCasePermutation(self, S):

        curr = [[]]
        for c in S:
            next = []
            for prefix in curr:
                permutation1 = prefix + [c]
                next.append(permutation1)
                if c.islower():
                    permutation2 = prefix + [c.upper()]
                    next.append(permutation2)
                elif c.isupper():
                    permutation2 = prefix + [c.lower()]
                    next.append(permutation2)
            curr = next

        ans = []
        for work_breakdown in curr:
            ans.append("".join(work_breakdown))

        return ans



Sol = Solution()
print Sol.letterCasePermutation("a1b2")

