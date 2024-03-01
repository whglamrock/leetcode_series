from collections import Counter, defaultdict
from copy import deepcopy
from typing import List, Dict

class Solution:
    def minStickers(self, stickers: List[str], target: str) -> int:
        letterToStickerCounters = defaultdict(list)
        for sticker in stickers:
            stickerCounter = Counter(sticker)
            for char in sticker:
                letterToStickerCounters[char].append(stickerCounter)

        return self.bfs(letterToStickerCounters, target)

    def serializeCharCount(self, stickerCounter: Dict[str, int]) -> str:
        serializedStrs = []
        for char in sorted(stickerCounter.keys()):
            serializedStrs.append(char + str(stickerCounter[char]))
        return ','.join(serializedStrs)

    def deserializeToCharCount(self, serializedCharCount: str) -> Dict[str, int]:
        tokens = serializedCharCount.split(',')
        charCount = {}
        for token in tokens:
            charCount[token[0]] = int(token[1:])
        return charCount

    def bfs(self, letterToStickerCounters: Dict[str, list], target: str) -> int:
        todo = {self.serializeCharCount(Counter(target))}
        visited = set()
        step = 0
        while todo:
            nextTodo = set()
            for serializedCharCount in todo:
                if not serializedCharCount:
                    return step
                if serializedCharCount in visited:
                    continue
                visited.add(serializedCharCount)
                currCharCount = self.deserializeToCharCount(serializedCharCount)
                for char in currCharCount:
                    if char not in letterToStickerCounters:
                        continue
                    for stickerCounter in letterToStickerCounters[char]:
                        nextCharCount = deepcopy(currCharCount)
                        # try to match as many chars as possible using one sticker
                        for stickerChar in stickerCounter:
                            if stickerChar not in nextCharCount:
                                continue
                            nextCharCount[stickerChar] -= stickerCounter[stickerChar]
                            if nextCharCount[stickerChar] <= 0:
                                del nextCharCount[stickerChar]
                        nextTodo.add(self.serializeCharCount(nextCharCount))

            todo = nextTodo
            step += 1

        return -1


sol = Solution()
print(sol.minStickers(["with", "example", "science"], "thehat"))
