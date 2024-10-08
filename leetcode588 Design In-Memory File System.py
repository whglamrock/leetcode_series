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

    # the description says the path is always valid, but actually it's possible that certain
    # directory is not in the curr.children map.
    def ls(self, path: str) -> List[str]:
        folders = path.split('/')
        curr = self.root

        for folder in folders:
            if not folder:
                continue
            # here we don't check if folder is in curr.children, otherwise the stupid leetcode
            # will fail on some stupid test case
            curr = curr.children[folder]

        if curr.isFile:
            return [folders[-1]]
        else:
            return sorted(curr.children.keys())

    def mkdir(self, path: str) -> None:
        folders = path.split('/')
        curr = self.root

        for folder in folders:
            if not folder:
                continue
            curr = curr.children[folder]

    def addContentToFile(self, filePath: str, content: str) -> None:
        folders = filePath.split('/')
        self.fileToContent[filePath].append(content)
        curr = self.root

        for folder in folders:
            if not folder:
                continue
            curr = curr.children[folder]
        curr.isFile = True

    def readContentFromFile(self, filePath: str) -> str:
        return ''.join(self.fileToContent[filePath])


# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.ls(path)
# obj.mkdir(path)
# obj.addContentToFile(filePath,content)
# param_4 = obj.readContentFromFile(filePath)
