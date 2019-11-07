
class Solution(object):
    def leastOpsExpressTarget(self, x, target):
        """
        :type x: int
        :type target: int
        :rtype: int
        """
        positive, negative, k = 0, 0, 0

        while target:
            target, cur = divmod(target, x)
            if k:
                positive, negative = min(cur * k + positive, (cur + 1) * k + negative), \
                                     min((x - cur) * k + positive, (x - cur - 1) * k + negative)
            else:
                positive, negative = cur * 2, (x - cur) * 2
            k += 1

        return min(positive, k + negative) - 1