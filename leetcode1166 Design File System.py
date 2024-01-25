from collections import defaultdict

class FileSystem:
    def __init__(self):
        self.pathToChildren = defaultdict(set)
        self.pathToValue = {}

    def createPath(self, path: str, value: int) -> bool:
        if not path or not path.startswith('/') or path == '/' or path in self.pathToValue:
            return False

        # P.S., for '/a/b' the first split substring would be ''
        folders = path.split('/')[1:]
        # no need to check parent if it's single layer
        if len(folders) == 1:
            self.pathToValue[path] = value
            return True

        parentPath = '/' + '/'.join(folders[:len(folders) - 1])
        if parentPath not in self.pathToValue:
            return False

        self.pathToValue[path] = value
        self.pathToChildren[parentPath].add(path)
        return True

    def get(self, path: str) -> int:
        if path not in self.pathToValue:
            return -1
        return self.pathToValue[path]


# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.createPath(path,value)
# param_2 = obj.get(path)
