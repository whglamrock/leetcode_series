from collections import defaultdict
from typing import List

class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        n = len(username)
        data = sorted(list(zip(username, timestamp, website)), key=lambda x: x[1])

        userToVisitedWebsites = defaultdict(list)
        for i in range(n):
            userToVisitedWebsites[data[i][0]].append(data[i][2])

        patternToCount = defaultdict(int)
        for websiteList in userToVisitedWebsites.values():
            currentPatterns = set()
            m = len(websiteList)
            for k in range(2, m):
                for j in range(1, k):
                    for i in range(j):
                        pattern = (websiteList[i], websiteList[j], websiteList[k])
                        currentPatterns.add(pattern)
            for pattern in currentPatterns:
                patternToCount[pattern] += 1

        maxCount = max(patternToCount.values())
        ans = []
        for pattern in patternToCount:
            if patternToCount[pattern] == maxCount:
                ans.append(list(pattern))
        return sorted(ans)[0]
