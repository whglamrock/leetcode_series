from typing import List

class Solution:
    def maxCandies(self, status: List[int], candies: List[int], keys: List[List[int]], containedBoxes: List[List[int]], initialBoxes: List[int]) -> int:
        openBoxes = set()
        boxesToOpen = set()
        for box in initialBoxes:
            if status[box] == 1:
                openBoxes.add(box)
            else:
                boxesToOpen.add(box)

        visited = set()
        numOfCandies = 0
        obtainedKeys = set()
        while openBoxes:
            nextOpenBoxes = set()
            for box in openBoxes:
                boxesToOpen.discard(box)
                if box in visited:
                    continue
                visited.add(box)
                numOfCandies += candies[box]
                for containedBox in containedBoxes[box]:
                    if containedBox not in visited and containedBox not in openBoxes:
                        boxesToOpen.add(containedBox)
                for key in keys[box]:
                    obtainedKeys.add(key)

            for boxToOpen in boxesToOpen:
                if boxToOpen in obtainedKeys or status[boxToOpen] == 1:
                    nextOpenBoxes.add(boxToOpen)

            openBoxes = nextOpenBoxes

        return numOfCandies
