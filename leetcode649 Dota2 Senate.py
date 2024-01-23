from collections import deque

class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        n = len(senate)
        radiants, dires = deque(), deque()
        for i in range(n):
            if senate[i] == 'R':
                radiants.append(i)
            else:
                dires.append(i)

        while radiants and dires:
            radiantIndex = radiants.popleft()
            direIndex = dires.popleft()
            if radiantIndex < direIndex:
                # because later on we need to compare who can announce victory
                # or this appended radiant index can be banned by smaller dire index
                radiants.append(n + radiantIndex)
            else:
                dires.append(n + direIndex)

        return 'Radiant' if radiants else 'Dire'
