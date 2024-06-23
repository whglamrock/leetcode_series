from collections import deque


# In below approach, all operations are amortized O(1). The linkedHashMap can also achieve similar effect, tho.
class AuthenticationManager:
    def __init__(self, timeToLive: int):
        self.timeToLive = timeToLive
        self.tokenQueue = deque()
        self.tokenIdToExpiry = {}

    def generate(self, tokenId: str, currentTime: int) -> None:
        self.popOutExpiredToken(currentTime)
        self.tokenIdToExpiry[tokenId] = currentTime + self.timeToLive
        self.tokenQueue.append([tokenId, currentTime + self.timeToLive])

    def renew(self, tokenId: str, currentTime: int) -> None:
        self.popOutExpiredToken(currentTime)
        if tokenId not in self.tokenIdToExpiry:
            return

        self.tokenIdToExpiry[tokenId] = currentTime + self.timeToLive
        self.tokenQueue.append([tokenId, currentTime + self.timeToLive])

    def countUnexpiredTokens(self, currentTime: int) -> int:
        self.popOutExpiredToken(currentTime)
        # there can be multiple elements in the queue with the same tokenId, all
        # of which have an unexpired time, so we need to count the keys of tokenId map
        return len(self.tokenIdToExpiry)

    def popOutExpiredToken(self, currentTime: int):
        while self.tokenQueue and self.tokenQueue[0][1] <= currentTime:
            expiredTokenId, expiredTime = self.tokenQueue.popleft()
            if expiredTokenId in self.tokenIdToExpiry and self.tokenIdToExpiry[expiredTokenId] <= currentTime:
                del self.tokenIdToExpiry[expiredTokenId]
