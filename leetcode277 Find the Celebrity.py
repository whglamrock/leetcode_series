# The knows API is already defined for you.
# return a bool, whether a knows b
def knows(a: int, b: int) -> bool:
    pass

# O(n) calls of knows API
class Solution:
    def findCelebrity(self, n: int) -> int:
        x = 0
        for i in range(n):
            if knows(x, i):
                # until this all previous x + 1 ~ i - 1 were ruled out
                x = i

        # make sure x doesn't know anyone
        for i in range(x):
            if knows(x, i):
                return -1

        # make sure everybody knows x
        for i in range(n):
            if not knows(i, x):
                return -1

        return x
