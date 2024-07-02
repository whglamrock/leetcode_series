from collections import defaultdict
from typing import List


class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        playerToWins = defaultdict(int)
        playerToLosses = defaultdict(int)
        for winner, loser in matches:
            playerToWins[winner] += 1
            playerToLosses[loser] += 1

        winners = []
        for player in playerToWins:
            if player not in playerToLosses:
                winners.append(player)

        losersWithOnlyOneLoss = []
        for player in playerToLosses:
            if playerToLosses[player] == 1:
                losersWithOnlyOneLoss.append(player)

        return [sorted(winners), sorted(losersWithOnlyOneLoss)]
