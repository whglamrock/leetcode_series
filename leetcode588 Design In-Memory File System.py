
from collections import defaultdict

# a really stupid question from baidu. what's the point of it if without complexity requirements?
# P.S., the sort in ls function can be saved using heapq (however, it takes more space and
#   each insertion take extra O(logN))

class TrieNode:
    def __init__(self):
        self.isFile = False
        self.children = defaultdict(TrieNode)



class FileSystem(object):
    def __init__(self):
        self.root = TrieNode()
        self.fileToContent = defaultdict(list)

    # the path is alwasy valid
    def ls(self, path):
        """
        :type path: str
        :rtype: List[str]
        """
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

    def mkdir(self, path):
        """
        :type path: str
        :rtype: None
        """
        directories = path.split('/')
        curr = self.root

        for directory in directories:
            if not directory:
                continue
            curr = curr.children[directory]

    def addContentToFile(self, filePath, content):
        """
        :type filePath: str
        :type content: str
        :rtype: None
        """
        directories = filePath.split('/')
        self.fileToContent[filePath].append(content)
        curr = self.root

        for directory in directories:
            if not directory:
                continue
            curr = curr.children[directory]
        curr.isFile = True

    def readContentFromFile(self, filePath):
        """
        :type filePath: str
        :rtype: str
        """
        return ''.join(self.fileToContent[filePath])



# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.ls(path)
# obj.mkdir(path)
# obj.addContentToFile(filePath,content)
# param_4 = obj.readContentFromFile(filePath)