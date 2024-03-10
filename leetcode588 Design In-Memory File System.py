from collections import defaultdict
from typing import List

# P.S., another solution is using heapq in a folder to sub-folder heapq list, which saves some time in ls function
class TrieNode:
    def __init__(self):
        self.isFile = False
        self.children = defaultdict(TrieNode)

class FileSystem(object):
    def __init__(self):
        self.root = TrieNode()
        self.fileToContent = defaultdict(list)

    # the path is always valid
    def ls(self, path: str) -> List[str]:
        directories = path.split('/')
        curr = self.root

        for directory in directories:
            if not directory:
                continue
            curr = curr.children[directory]

        if curr.isFile:
            return [directories[-1]]
        else:
            return sorted(curr.children.keys())

    def mkdir(self, path: str) -> None:
        directories = path.split('/')
        curr = self.root

        for directory in directories:
            if not directory:
                continue
            curr = curr.children[directory]

    def addContentToFile(self, filePath: str, content: str) -> None:
        directories = filePath.split('/')
        self.fileToContent[filePath].append(content)
        curr = self.root

        for directory in directories:
            if not directory:
                continue
            curr = curr.children[directory]
        curr.isFile = True

    def readContentFromFile(self, filePath: str) -> str:
        return ''.join(self.fileToContent[filePath])


# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.ls(path)
# obj.mkdir(path)
# obj.addContentToFile(filePath,content)
# param_4 = obj.readContentFromFile(filePath)
