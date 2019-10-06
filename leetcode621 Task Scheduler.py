
# see explanation: https://discuss.leetcode.com/topic/92852/concise-java-solution-o-n-time-o-26-space/28
    # Idea is: use the tasks/letters with most count as "frames" and insert the rest of letters in between.
    # e.g., for AACCCBEEE 2, 'CE' is the frame; insert with the highest frequency, result is CE A B CE A CE.
    # let m = number of frames, so:
    # 1) when n is big enough the first m - 1 buckets' length is (m - 1) * (n + 1);
    #    the length of final bucket = len(single frame) = 25 - i;
    # 2) when n is not big enough, then the cool-down time is useless, the ans = len(tasks)

class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        if not tasks:
            return 0

        taskCount = [0] * 26
        for task in tasks:
            taskCount[ord(task) - ord('A')] += 1
        taskCount.sort()

        i = 25
        while i >= 0 and taskCount[i] == taskCount[-1]:
            i -= 1

        return max(len(tasks), (taskCount[-1] - 1) * (n + 1) + 25 - i)



Sol = Solution()
tasks = ['A', 'B', 'A', 'C', 'A', 'E', 'A', 'D', 'B']
n = 4
print Sol.leastInterval(tasks, n)



'''
from collections import defaultdict

# use a map to record each task type's idle status
# always arrange the task type with most tasks left

class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        taskToIdle = {}
        taskCount = defaultdict(int)
        for task in tasks:
            taskCount[task] += 1
            taskToIdle[task] = 0

        ans = 0
        while taskCount:
            arrangableTasks = self.getArrangableTasks(taskToIdle, taskCount)
            # update the taskToIdle before actually arranging
            self.updateIdleTime(taskToIdle)
            if arrangableTasks:
                task = self.arrangeTaskWithMostCount(arrangableTasks, taskCount)
                taskToIdle[task] = n
            ans += 1

        return ans

    # not only get the task but also update the taskCount
    def arrangeTaskWithMostCount(self, arrangableTasks, taskCount):
        maxCount = 0
        res = None
        for task in arrangableTasks:
            count = taskCount[task]
            if count > maxCount:
                maxCount = count
                res = task

        taskCount[res] -= 1
        if taskCount[res] == 0:
            del taskCount[res]
        return res

    def updateIdleTime(self, taskToIdle):
        for task in taskToIdle:
            taskToIdle[task] = max(0, taskToIdle[task] - 1)

    def getArrangableTasks(self, taskToIdle, taskCount):
        arrangableTasks = []
        # O(26)
        for taskType in taskCount:
            if taskToIdle[taskType] == 0:
                arrangableTasks.append(taskType)
        return arrangableTasks
'''