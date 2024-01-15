from collections import defaultdict
from typing import List

class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        winnerToLosers, loserToWinners = defaultdict(set), defaultdict(set)
        for winner, loser in matches:
            winnerToLosers[winner].add(loser)
            loserToWinners[loser].add(winner)

        playersNeverLost, playersLostOnce = [], []
        for player in sorted(winnerToLosers.keys()):
            if player not in loserToWinners:
                playersNeverLost.append(player)
        for player in sorted(loserToWinners.keys()):
            if len(loserToWinners[player]) == 1:
                playersLostOnce.append(player)

        return [playersNeverLost, playersLostOnce]
