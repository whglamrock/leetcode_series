
# one-digit number: 9 nums; two-digit number: 90 nums...

class Solution(object):
    def findNthDigit(self, n):

        i = 0
        accum = 0   # to acuumulate the number of cycles (per cycle per number of digits)
        while accum < n:
            accum += 9 * (10 ** i) * (i + 1)
            i += 1

        i -= 1
        accum -= 9 * (10 ** i) * (i + 1)
        order = n - accum   # the actual number is in the middle of a cycle (extreme case at the end)
        orderofnum = order / (i + 1)  # e.g. find position of the actual num after 99, like 103 is
        # the fourth num after 99.
        remain = order % (i + 1)  # the digit postion is in the middle of next number when remain > 0
        start = 10 ** i
        if remain == 0:
            actualnum = start + orderofnum - 1
            return int(str(actualnum)[-1])
        else:
            actualnum = start + orderofnum
            return int(str(actualnum)[remain - 1])



Sol = Solution()
print Sol.findNthDigit(1000)
