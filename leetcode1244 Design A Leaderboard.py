from collections import defaultdict

class Leaderboard:
    def __init__(self):
        self.playerToScore = defaultdict(int)
        self.scoreToPlayerCount = defaultdict(int)

    def addScore(self, playerId: int, score: int) -> None:
        if playerId in self.playerToScore:
            originalScore = self.playerToScore[playerId]
            self.scoreToPlayerCount[originalScore] -= 1
            if not self.scoreToPlayerCount[originalScore]:
                del self.scoreToPlayerCount[originalScore]
        self.playerToScore[playerId] += score
        currScore = self.playerToScore[playerId]
        self.scoreToPlayerCount[currScore] += 1

    def top(self, k: int) -> int:
        sortedScores = sorted(self.scoreToPlayerCount.keys(), key=lambda x: -x)
        kSum = 0
        for score in sortedScores:
            if k == 0:
                break
            numOfPlayersToAdd = min(k, self.scoreToPlayerCount[score])
            kSum += numOfPlayersToAdd * score
            k -= numOfPlayersToAdd
        return kSum

    def reset(self, playerId: int) -> None:
        score = self.playerToScore[playerId]
        self.scoreToPlayerCount[score] -= 1
        if not self.scoreToPlayerCount[score]:
            del self.scoreToPlayerCount[score]
        del self.playerToScore[playerId]


# Your Leaderboard object will be instantiated and called as such:
# obj = Leaderboard()
# obj.addScore(playerId,score)
# param_2 = obj.top(K)
# obj.reset(playerId)
