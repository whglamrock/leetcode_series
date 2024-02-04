from typing import List, Dict
from collections import defaultdict

# check: https://leetcode.com/problems/maximum-employees-to-be-invited-to-a-meeting/solutions/1661178/python-explanation-with-pictures/
class Solution:
    def maximumInvitations(self, favorite: List[int]) -> int:
        # case 1: circle. find the length of max circle
        maxCircle = self.dfsToFindLenOfMaxCircle(favorite)

        # case 2: pairs, each of which has two arms (left and right).
        # Then find the length of longest such left/right arm
        pairs = set()
        for i in range(len(favorite)):
            if favorite[favorite[i]] == i:
                pair = (min([i, favorite[i]]), max([i, favorite[i]]))
                pairs.add(pair)

        followers = defaultdict(list)
        for i in range(len(favorite)):
            followers[favorite[i]].append(i)

        sumOfExtendedLenFromPairs = 0
        for a, b in pairs:
            maxLenOfArmToA = self.findLenOfLongestArm(a, b, followers)
            maxLenOfArmToB = self.findLenOfLongestArm(b, a, followers)
            sumOfExtendedLenFromPairs += 2 + maxLenOfArmToA + maxLenOfArmToB

        # select the larger one as the answer.
        return max(maxCircle, sumOfExtendedLenFromPairs)

    def dfsToFindLenOfMaxCircle(self, favorite: List[int]) -> int:
        n = len(favorite)
        visited = set()
        lenOfMaxCircle = 0

        for i in range(n):
            if i in visited:
                continue

            curr = i
            currVisited = set()
            while curr not in currVisited:
                currVisited.add(curr)
                visited.add(curr)
                curr = favorite[curr]

            # found a circle. Note that curr may != i
            # It's also possible that we don't find any circle
            if curr in currVisited:
                currLenOfCircle = len(currVisited)
                start = i
                while curr != start:
                    currLenOfCircle -= 1
                    start = favorite[start]
                lenOfMaxCircle = max(lenOfMaxCircle, currLenOfCircle)

        return lenOfMaxCircle

    # it's impossible that the other end of the arm is connected to another pair
    def findLenOfLongestArm(self, startPoint: int, nodeToAvoid: int, followers: Dict[int, List[int]]) -> int:
        maxLenOfArm = 0
        todo = {startPoint}
        while todo:
            nextTodo = set()
            for node in todo:
                for follower in followers[node]:
                    if follower != nodeToAvoid:
                        nextTodo.add(follower)
            todo = nextTodo
            if todo:
                maxLenOfArm += 1
        return maxLenOfArm


print(Solution().maximumInvitations(favorite=[2, 2, 1, 2]))
print(Solution().maximumInvitations(favorite=[1, 2, 0]))
print(Solution().maximumInvitations(favorite=[3, 0, 1, 4, 1]))
