
# the key is to think of: the optimal way to warm the house is to use two nearest heaters.

class Solution(object):
    def findRadius(self, houses, heaters):

        heaters.sort()

        # find two consecutive heaters that can warm the house
        def binarysearch(x, heaters):
            l, r = 0, len(heaters)
            # at last, l will == r
            while l < r:
                mid = l + (r - l) / 2
                if heaters[mid] < x:
                    l = mid + 1
                else:
                    r = mid
            if l == len(heaters) - 1 and x > heaters[-1]:
                return len(heaters) - 1
            return l - 1

        radius = 0
        for x in houses:
            i = binarysearch(x, heaters)
            if i == -1:
                radius = max(radius, abs(heaters[0] - x))
            elif i == len(heaters) - 1:
                radius = max(radius, abs(heaters[-1] - x))
            else:
                dist1 = abs(heaters[i] - x)
                dist2 = abs(heaters[i + 1] - x)
                radius = max(radius, min(dist1, dist2))

        return radius