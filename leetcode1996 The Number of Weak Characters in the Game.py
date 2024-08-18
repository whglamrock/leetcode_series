from collections import deque
from typing import List, Tuple


# You have to come up with O(NlogN) solution
class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        properties.sort()
        maxDefense = 0
        attackAndMaxDefense = deque()
        for i in range(len(properties) - 1, -1, -1):
            maxDefense = max(maxDefense, properties[i][1])
            attackAndMaxDefense.appendleft([properties[i][0], maxDefense])

        count = 0
        for i in range(len(properties) - 1, -1, -1):
            minBiggerAttack, maxDefenceOfMinBiggerAttack = self.findMinAttackBiggerThan(attackAndMaxDefense, properties[i][0])
            if maxDefenceOfMinBiggerAttack > properties[i][1]:
                count += 1

        return count

    def findMinAttackBiggerThan(self, attackAndMaxDefense: List[List[int]], target: int) -> Tuple[int, int]:
        l, r = 0, len(attackAndMaxDefense) - 1
        while l <= r:
            m = (l + r) // 2
            attack, defense = attackAndMaxDefense[m]
            if l == r:
                if attack > target:
                    return attack, defense
                return -1, -1
            if attack <= target:
                l = m + 1
            else:
                r = m

        return -1, -1
