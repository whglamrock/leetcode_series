from collections import defaultdict

class TrieNode:
    def __init__(self):
        self.count = 0
        self.children = defaultdict(TrieNode)

class Trie:
    def __init__(self):
        self.wordToNode = {}
        self.nodeToWord = {}
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root
        for char in word:
            curr = curr.children[char]
        curr.count += 1
        self.wordToNode[word] = curr
        self.nodeToWord[curr] = word

    def countWordsEqualTo(self, word: str) -> int:
        if word not in self.wordToNode:
            return 0
        return self.wordToNode[word].count

    def countWordsStartingWith(self, prefix: str) -> int:
        curr = self.root
        for char in prefix:
            if char not in curr.children:
                return 0
            curr = curr.children[char]

        # bfs
        todo = {curr}
        foundWords = set()
        while todo:
            nextTodo = set()
            for node in todo:
                if node.count > 0:
                    foundWords.add(self.nodeToWord[node])
                for nextNode in node.children.values():
                    nextTodo.add(nextNode)
            todo = nextTodo

        numOfWordsStartsWithPrefix = 0
        for word in foundWords:
            numOfWordsStartsWithPrefix += self.wordToNode[word].count
        return numOfWordsStartsWithPrefix

    def erase(self, word: str) -> None:
        if word not in self.wordToNode:
            return
        node = self.wordToNode[word]
        self.wordToNode[word].count -= 1
        if self.wordToNode[word].count == 0:
            del self.wordToNode[word]
            del self.nodeToWord[node]


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.countWordsEqualTo(word)
# param_3 = obj.countWordsStartingWith(prefix)
# obj.erase(word)
