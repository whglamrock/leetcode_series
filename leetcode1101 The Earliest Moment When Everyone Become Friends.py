from collections import defaultdict
from typing import Dict, List

# Below we always merge the smaller group to the bigger one; the actual runtime should be
# similar to the typical union-find solution
class Solution:
    def earliestAcq(self, logs: List[List[int]], n: int) -> int:
        # sort by timestamp
        logs.sort()
        personToGroup = {}
        groupToPersons = defaultdict(set)
        groupNumber = 0
        for time, person1, person2 in logs:
            if person1 in personToGroup and person2 in personToGroup:
                if personToGroup[person1] == personToGroup[person2]:
                    continue
                # person 1 & 2 belong to different group
                self.merge2Groups(person1, person2, personToGroup, groupToPersons)
            elif person1 not in personToGroup and person2 not in personToGroup:
                personToGroup[person1] = groupNumber
                personToGroup[person2] = groupNumber
                groupToPersons[groupNumber] = {person1, person2}
                groupNumber += 1
            elif person1 in personToGroup:
                personToGroup[person2] = personToGroup[person1]
                groupToPersons[personToGroup[person1]].add(person2)
            else:
                personToGroup[person1] = personToGroup[person2]
                groupToPersons[personToGroup[person2]].add(person1)

            if len(personToGroup) == n and len(groupToPersons) == 1:
                return time

        return -1

    def merge2Groups(self, person1: int, person2: int, personToGroup: Dict[int, int], groupToPersons: Dict[int, set]):
        group1, group2 = personToGroup[person1], personToGroup[person2]
        # making sure we always merge the smaller group into the bigger one
        if len(groupToPersons[group1]) < len(groupToPersons[group2]):
            person1, person2 = person2, person1

        groupNumber = personToGroup[person1]
        groupNumberToDiscard = personToGroup[person2]
        for person in groupToPersons[groupNumberToDiscard]:
            personToGroup[person] = groupNumber
            groupToPersons[groupNumber].add(person)

        del groupToPersons[groupNumberToDiscard]
