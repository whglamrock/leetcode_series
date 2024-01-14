
# math idea from here: https://leetcode.com/problems/bulb-switcher/solutions/77104/math-solution/
# any number that has even number of dividers will be turned off. Only a square number has odd number of dividers
import math
class Solution(object):
    def bulbSwitch(self, n: int) -> int:
        return int(math.sqrt(n))
