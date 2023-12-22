from collections import defaultdict, Counter, deque


class Solution(object):
    def minStickers(self, stickers, target):
        """
        :type stickers: List[str]
        :type target: str
        :rtype: int
        """
        targetCounter = Counter(target)
        letterToStickerCounterList = defaultdict(list)
        for sticker in stickers:
            stickerCounter = Counter(sticker)
            for char in sticker:
                letterToStickerCounterList[char].append(stickerCounter)

        return self.bfs(targetCounter, letterToStickerCounterList)

    def counterToStr(self, counter):
        return ''.join([k * v for k, v in counter.items()])

    def bfs(self, targetCounter, letterToStickerCounterList):
        queue = deque([(targetCounter, 0)])
        visited = set()

        while queue:
            currTargetCounter, step = queue.popleft()
            if not currTargetCounter:
                return step

            currTargetStr = self.counterToStr(currTargetCounter)
            if currTargetStr in visited:
                continue
            visited.add(currTargetStr)

            # try to satisfy one letter at a time
            randomLetter = list(currTargetCounter.keys())[0]
            for stickerCounter in letterToStickerCounterList[randomLetter]:
                curr_copy = currTargetCounter.copy()
                # when do bfs, deduct other letters as well
                for letter in stickerCounter.keys():
                    curr_copy[letter] -= stickerCounter[letter]
                    # this also includes the case where the sticker's letter is not in the current target
                    if curr_copy[letter] <= 0:
                        del curr_copy[letter]
                queue.append((curr_copy, step + 1))

        return -1


sol = Solution()
print(sol.minStickers(["with", "example", "science"], "thehat"))
