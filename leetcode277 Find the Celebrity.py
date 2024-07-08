
# The knows API is already defined for you. It return a bool, whether a knows b.
def knows(a: int, b: int) -> bool:
    pass


# Intuition:
# 1) find a candidate that don't know anyone in range (candidate, n] -> the "if knows(candidate, i)" logic will make it
# work and we don't have to worry about having 2 candidates (x1 < x2) that both satisfy the requirement
# knows(x, i (x <= i < n)) == False. Because x1 < x2 and if x1 doesn't know x2 there is no way x2 is the celebrity
# 2) make sure the candidate doesn't know anyone in range [0, candidate)
# 3) make sure everybody knows candidate
class Solution:
    def findCelebrity(self, n: int) -> int:
        candidate = 0
        for i in range(n):
            # if until certain j all knows(candidate, x) where 0 <= x <= j - 1 have been false it means all j - 1 persons are not candidate
            if knows(candidate, i):
                candidate = i

        # make sure candidate doesn't know anyone < candidate
        for i in range(candidate):
            if knows(candidate, i):
                return -1

        # make sure everybody knows candidate
        for i in range(n):
            if not knows(i, candidate):
                return -1

        return candidate
