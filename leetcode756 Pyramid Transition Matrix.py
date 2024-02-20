from collections import defaultdict
from typing import List

class Solution:
    def pyramidTransition(self, bottom: str, allowed: List[str]) -> bool:
        twoLetterToOneLetters = defaultdict(set)
        for pattern in allowed:
            twoLetterToOneLetters[pattern[:2]].add(pattern[2])

        todo = {bottom}
        while todo:
            if len(list(todo)[0]) == 1:
                return True

            nextTodo = set()
            for levelCandidate in todo:
                # use a curr & next array for backtracking
                curr = ['']
                for i in range(1, len(levelCandidate)):
                    next = []
                    twoLetter = levelCandidate[i - 1] + levelCandidate[i]
                    if twoLetter not in twoLetterToOneLetters:
                        continue
                    for currSubstr in curr:
                        for oneLetter in twoLetterToOneLetters[twoLetter]:
                            next.append(currSubstr + oneLetter)
                    curr = next
                if curr and len(curr[0]) == len(levelCandidate) - 1:
                    for nextLevelCandidate in curr:
                        nextTodo.add(nextLevelCandidate)

            todo = nextTodo

        return False
