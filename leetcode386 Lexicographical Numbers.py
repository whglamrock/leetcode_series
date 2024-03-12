from typing import List

# The idea is: in lexicographical sorting, when generating next number we wanna keep the prefix same as much as possible.
# At first, we try to add a 0 digit after the previous number, if it's out of range, we do //10 and +1 operations. And if
# the new number has any 0 at the end, we must remove it (to get next lexicographically smallest).
class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        ans = [1]
        while len(ans) < n:
            newNum = ans[-1] * 10
            while newNum > n:
                newNum = (newNum // 10) + 1
                # deal with case like 199 + 1 = 200 when we need to restart from 2.
                while newNum % 10 == 0:
                    newNum //= 10
            ans.append(newNum)

        return ans
