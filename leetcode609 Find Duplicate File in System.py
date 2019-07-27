
from collections import defaultdict

class Solution(object):
    def findDuplicate(self, paths):
        """
        :type paths: List[str]
        :rtype: List[List[str]]
        """
        fileContentsToPaths = defaultdict(list)
        for path in paths:
            data = path.split(" ")
            root = data[0]
            for fileNameAndContent in data[1:]:
                miscellaneous = fileNameAndContent.split('(')
                fileName, content = miscellaneous[0], miscellaneous[1][:-1]
                fileContentsToPaths[content].append(root + '/' + fileName)

        ans = []
        for key, value in fileContentsToPaths.items():
            if len(value) > 1:
                ans.append(value)

        return ans



print Solution().findDuplicate(paths=["root/a 1.txt(abcd) 2.txt(efgh)", "root/c 3.txt(abcd)", "root/c/d 4.txt(efgh)", "root 4.txt(efgh)"])
