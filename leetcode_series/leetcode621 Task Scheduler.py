
# see my explanation: https://discuss.leetcode.com/topic/92852/concise-java-solution-o-n-time-o-26-space/28
# the priorityQueue solution is actually more troublesome, while the logic is similar.

class Solution(object):
    def leastInterval(self, tasks, n):

        c = [0] * 26
        for task in tasks:
            c[ord(task) - ord('A')] += 1
        c.sort()

        i = 25
        while i >= 0 and c[i] == c[25]:
            i -= 1

        return max(len(tasks), (c[25] - 1) * (n + 1) + 25 - i)



Sol = Solution()
tasks = ['A', 'B', 'A', 'C', 'A', 'E', 'A', 'D', 'B']
n = 4
print Sol.leastInterval(tasks, n)
