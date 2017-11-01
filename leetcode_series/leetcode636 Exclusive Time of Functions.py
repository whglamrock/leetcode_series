
class Solution(object):
    def exclusiveTime(self, n, logs):

        if not logs:
            return []

        # only saves the f_id
        stack = []
        # each ans[i] is accumulate by adding up all small intervals and gaps between intervals
        ans = [0] * n
        # record the time stamp of each move (both start and end)
        prev_time = 0

        for log in logs:
            f_id, status, time = log.split(':')
            f_id, time = int(f_id), int(time)
            if status == 'start':
                if stack:   # stack[-1]'s status is always 'start'
                    ans[stack[-1]] += time - prev_time
                stack.append(f_id)
                prev_time = time
            else:
                # ans[stack[-1]] won't be changed afterwards
                ans[stack[-1]] += time + 1 - prev_time
                stack.pop()
                prev_time = time + 1

        return ans



n = 2
logs = ["0:start:0", "1:start:2", "1:end:5", "0:end:6"]
Sol = Solution()
print Sol.exclusiveTime(n, logs)
