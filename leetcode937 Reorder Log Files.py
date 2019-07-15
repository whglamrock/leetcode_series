
# time complexity: # O(log(len(letterLogs)) * avgLen(letterLogs[i]))

class Solution(object):
    def reorderLogFiles(self, logs):
        """
        :type logs: List[str]
        :rtype: List[str]
        """
        if not logs:
            return []

        letterLogs = []
        digitLogs = []

        for log in logs:
            logWords = log.split(' ')
            if logWords[1][0].isdigit():
                digitLogs.append(logWords)
            else:
                # here we will consume some extra time complexity but it doesn't change the totol time complexity because we are sorting letterLogs list anyways
                letterLogs.append(logWords[1:] + [logWords[0]])

        # O(log(len(letterLogs)) * avgLen(letterLogs[i]))
        letterLogs.sort()
        ans = []
        for logWords in letterLogs:
            ans.append(' '.join([logWords[-1]] + logWords[:len(logWords) - 1]))
        for logWords in digitLogs:
            ans.append(' '.join(logWords))

        return ans



print Solution().reorderLogFiles(logs = ["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo"])