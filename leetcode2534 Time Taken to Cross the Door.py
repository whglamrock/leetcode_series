from collections import deque
from typing import List

class Solution:
    def timeTaken(self, arrival: List[int], state: List[int]) -> List[int]:
        enterQueue, exitQueue = deque(), deque()
        for i in range(len(arrival)):
            if state[i] == 0:
                enterQueue.append([arrival[i], i])
            else:
                exitQueue.append([arrival[i], i])

        ans = [0] * len(arrival)
        prevPerson = None
        prevTime = None
        while enterQueue and exitQueue:
            if prevTime is None or min(enterQueue[0][0], exitQueue[0][0]) > prevTime + 1:
                if exitQueue[0][0] <= enterQueue[0][0]:
                    time, i = exitQueue.popleft()
                    prevPerson = 'exit'
                else:
                    time, i = enterQueue.popleft()
                    prevPerson = 'enter'
                ans[i] = time
                prevTime = time
            else:
                if prevPerson == 'enter' and enterQueue[0][0] <= prevTime + 1:
                    time, i = enterQueue.popleft()
                elif prevPerson == 'exit' and exitQueue[0][0] <= prevTime + 1:
                    time, i = exitQueue.popleft()
                else:
                    if exitQueue[0][0] <= enterQueue[0][0]:
                        time, i = exitQueue.popleft()
                        prevPerson = 'exit'
                    else:
                        time, i = enterQueue.popleft()
                        prevPerson = 'enter'
                realCrossTime = max(time, prevTime + 1)
                ans[i] = realCrossTime
                prevTime = realCrossTime

        if exitQueue:
            q = exitQueue
        else:
            q = enterQueue
        while q:
            time, i = q.popleft()
            realCrossTime = max(time, prevTime + 1) if prevTime is not None else time
            ans[i] = realCrossTime
            prevTime = realCrossTime

        return ans


print(Solution().timeTaken(arrival=[0, 1, 1, 2, 4], state=[0, 1, 0, 0, 1]))
