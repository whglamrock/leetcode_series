
# There is not really "shortcut" solution for this problem: you can't find all index pairs where you can exchange them,
# and return len(exchangeIndexes) // 2 + len(s1) - len(unchangedIndexes) - len(exchangeIndexes) - 1.
# The reason why using the above approach is wrong is because you can generate new s1 permutation where exchangeable
# index pair exists when you swap indexes that initially are not "exchangeIndexes".
# E.g., consider s1 = aabbccddee, and s2 = dcacbedbae
class Solution:
    def kSimilarity(self, s1: str, s2: str) -> int:
        # bfs
        todo = {s1}
        distance = 0
        while todo:
            next = set()
            for string in todo:
                if string == s2:
                    return distance
                next = next.union(self.generateNextPermutations(string, s2))
            todo = next
            distance += 1

        return distance

    # greedy BFS: if we found exchangeable index pairs, we don't look for other permutations
    def generateNextPermutations(self, s1: str, s2: str) -> set:
        i = 0
        while i < len(s1) and s1[i] == s2[i]:
            i += 1

        # look for exchange
        foundExchange = False
        for j in range(i + 1, len(s1)):
            if s1[j] == s2[i] and s2[j] == s1[i]:
                foundExchange = True
                break
        if foundExchange:
            return {self.swapIndexes(s1, i, j)}

        permutations = set()
        for j in range(i + 1, len(s1)):
            if s1[j] == s2[i]:
                permutations.add(self.swapIndexes(s1, i, j))
        return permutations

    def swapIndexes(self, s: str, i: int, j: int) -> str:
        return s[:i] + s[j] + s[i + 1:j] + s[i] + s[j + 1:]


print(Solution().kSimilarity("aabbccddee", "dcacbedbae"))
