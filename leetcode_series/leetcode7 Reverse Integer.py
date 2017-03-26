
# too easy. no explanation
# but be aware of all edge cases to avoid overflow

class Solution(object):
    def reverse(self, x):

        if abs(x) >= 2147483647:
            return 0

        result = 0
        pos_x = abs(x)
        while pos_x:
            result = result * 10 + pos_x % 10
            pos_x /= 10

        if result >= 2147483647:
            return 0

        return result if x >= 0 else -result