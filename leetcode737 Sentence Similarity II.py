
class Solution(object):
    def areSentencesSimilarTwo(self, words1, words2, pairs):
        """
        :type words1: List[str]
        :type words2: List[str]
        :type pairs: List[List[str]]
        :rtype: bool
        """
        if len(words1) != len(words2):
            return False

        parent = {}
        for i, j in pairs:
            parent[i] = i
            parent[j] = j

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            parent[find(x)] = find(y)

        for i, j, in pairs:
            union(i, j)

        for word1, word2 in zip(words1, words2):
            if word1 == word2:
                continue
            if word1 not in parent or word2 not in parent:
                return False
            if find(word1) != find(word2):
                return False

        return True



print Solution().areSentencesSimilarTwo(
    ["I", "have", "enjoyed", "happy", "thanksgiving", "holidays"],

    ["I", "have", "enjoyed", "happy", "thanksgiving", "holidays"],

    [["great", "good"], ["extraordinary", "good"], ["well", "good"], ["wonderful", "good"], ["excellent", "good"],
     ["fine", "good"], ["nice", "good"], ["any", "one"], ["some", "one"], ["unique", "one"], ["the", "one"],
     ["an", "one"], ["single", "one"], ["a", "one"], ["truck", "car"], ["wagon", "car"], ["automobile", "car"],
     ["auto", "car"], ["vehicle", "car"], ["entertain", "have"], ["drink", "have"], ["eat", "have"], ["take", "have"],
     ["fruits", "meal"], ["brunch", "meal"], ["breakfast", "meal"], ["food", "meal"], ["dinner", "meal"],
     ["super", "meal"], ["lunch", "meal"], ["possess", "own"], ["keep", "own"], ["have", "own"], ["extremely", "very"],
     ["actually", "very"], ["really", "very"],["super", "very"]
     ]
)



'''
# DFS approach
class Solution(object):
    def areSentencesSimilarTwo(self, words1, words2, pairs):
        """
        :type words1: List[str]
        :type words2: List[str]
        :type pairs: List[List[str]]
        :rtype: bool
        """
        if words1 is None or words2 is None:
            return False
        if len(words1) != len(words2):
            return False

        # build the graph
        graph = {}
        for i, j in pairs:
            if i not in graph:
                graph[i] = set()
                graph[i].add(i)
            if j not in graph:
                graph[j] = set()
                graph[j].add(j)
            graph[i].add(j)
            graph[j].add(i)

        # print graph
        for word1, word2 in zip(words1, words2):
            if word1 == word2:
                continue
            if word1 not in graph or word2 not in graph:
                return False
            if not self.dfs(word1, word2, graph, set()) and not self.dfs(word2, word1, graph, set()):
                return False

        return True

    def dfs(self, start, end, graph, visited):
        if start == end:
            return True
        if start in visited:
            return False
        visited.add(start)
        for neighbor in graph[start]:
            if neighbor not in visited:
                if self.dfs(neighbor, end, graph, visited):
                    return True
                visited.add(neighbor)
        return False
'''
