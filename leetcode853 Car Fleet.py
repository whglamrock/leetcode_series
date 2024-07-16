from typing import List


# Intuition: if B can catch A before target, and C can catch B before target, then C can definitely catch A because
# B's speed will reduce to A's speed after B & A form a group. Another important realization is: the head car that
# passes the finish line won't need to change the speed.
# So we sort the cars by is distance to the target and calculate the time needed to reach the target.
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        times = [(target - p) / s for p, s in sorted(zip(position, speed), reverse=True)]
        # print(times)
        ans, curr = 0, 0
        for time in times:
            # this means the current car won't be able to catch any previous cars
            if time > curr:
                ans += 1
                curr = time

        return ans
