
from collections import deque

class Solution(object):
    def reorderLogFiles(self, logs):
        """
        :type logs: List[str]
        :rtype: List[str]
        """
        if not logs:
            return []

        letterLogs, digitLogs = [], []
        for log in logs:
            # identifier is a string, actualLog is a list of strings
            tokens = self.parseLog(log)
            if tokens[0][0].isdigit():
                digitLogs.append(tokens)
            else:
                letterLogs.append(tokens)

        letterLogs.sort()

        ans = []
        for log in letterLogs:
            ans.append(self.rebuildLog(log))
        for log in digitLogs:
            ans.append(self.rebuildLog(log))

        return ans

    def rebuildLog(self, log):
        identifier = log.pop()
        log.appendleft(identifier)
        return ' '.join(log)

    def parseLog(self, log):
        tokens = deque(log.split(' '))
        identifier = tokens.popleft()
        tokens.append(identifier)
        return tokens



print Solution().reorderLogFiles(["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo"])