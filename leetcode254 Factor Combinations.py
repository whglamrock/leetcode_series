
# Backtracking

class Solution(object):
    def getFactors(self, n):

        todo, combis = [(n, 2, [])], []   # the smallest factor starts from 2.
        while todo:
            n, i, combi = todo.pop()

            while i * i <= n:   # when checking a number's factor, alwasy need to only check from 2 to sqrt(number)
                if n % i == 0:
                    combis += combi + [i, n/i],   # adds one feasible factor combination to the answer list.
                    todo += (n/i, i, combi+[i]),    # n/i marks the remaining 'n' that hasn't been divided yet;
                    # i marks the previous factor from which the new 'i' will start in the next loop;
                    # new combi = combi+[i] marks the factors that already 'stripped' from the original n
                i += 1

        return combis



Sol = Solution()
print Sol.getFactors(180)








