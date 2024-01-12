
# it's such a stupidly annoying question with a lot of edge cases. what's fucking point of such question?
class Solution:
    def isReachableAtTime(self, sx: int, sy: int, fx: int, fy: int, t: int) -> bool:
        minTime = max(abs(fy - sy), abs(fx - sx))
        maxTime = abs(fy - sy) + abs(fx - sx)

        # 1) if t is in [minTime, maxTime] it doesn't need to go backwards
        # 2) if t < minTime, it cannot finish
        # 3) if t > maxTime, it needs to go backwards sometimes since it has to keep moving.
        # Since it can move 8 directions, when not (fx == sx and fy == sy), you can prove that
        # no matter how much extra time you have you can always use (t - maxTime) to move to destination
        # but for (fx == sx and fy == sy), (t - maxTime) cannot be 1
        if minTime <= t <= maxTime:
            return True
        elif t < minTime:
            return False
        else:
            if fx == sx and fy == sy:
                return t > 1
            return True
