class Solution(object):
    def lastRemaining(self, n):

        left = True
        head = 1
        remaining = n
        step = 1
        while remaining > 1:
            if left or remaining % 2 == 1:
                head += step
            remaining /= 2
            step *= 2
            left = not left

        return head

Sol = Solution()
print Sol.lastRemaining(8)

