
from collections import defaultdict

# a really stupid question from baidu. what's the point of it if without complexity requirements?
# P.S., the sort in ls function can be saved using heapq (however, it takes more space and
#   each insertion take extra O(logN))

class TrieNode:
    def __init__(self):

        self.isfile = False
        self.children = defaultdict(TrieNode)


class FileSystem(object):
    def __init__(self):

        self.root = TrieNode()
        self.filetocontent = defaultdict(str)

    def ls(self, path):

        path = path.split('/')
        curr = self.root
        for directory in path:
            if not directory: continue
            curr = curr.children[directory]
        if curr.isfile:
            return [path[-1]]
        else:
            return sorted(curr.children.keys())

    def mkdir(self, path):

        curr = self.root
        path = path.split('/')

        for directory in path:
            if not directory: continue
            curr = curr.children[directory]

    def addContentToFile(self, filePath, content):

        curr = self.root
        absolutepath = filePath
        filePath = filePath.split('/')
        for directory in filePath:
            if not directory: continue
            curr = curr.children[directory]
        curr.isfile = True
        self.filetocontent[absolutepath] += content

    def readContentFromFile(self, filePath):

        return self.filetocontent[filePath]



# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.ls(path)
# obj.mkdir(path)
# obj.addContentToFile(filePath,content)
# param_4 = obj.readContentFromFile(filePath)