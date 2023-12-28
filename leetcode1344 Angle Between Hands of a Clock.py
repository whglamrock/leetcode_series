class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        minuteAngle = minutes * 6
        hourAngle = hour * 30 + minutes / 2
        return min(abs(minuteAngle - hourAngle), 360 - abs(minuteAngle - hourAngle))


print(Solution().angleClock(hour=12, minutes=30))
print(Solution().angleClock(hour=3, minutes=30))
print(Solution().angleClock(hour=3, minutes=15))
