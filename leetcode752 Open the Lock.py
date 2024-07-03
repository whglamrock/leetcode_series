from typing import List


class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        deadends = set(deadends)
        todo = {'0000'}
        visited = set()
        steps = 0
        while todo:
            nextTodo = set()
            for combination in todo:
                if combination == target:
                    return steps
                if combination in deadends or combination in visited:
                    continue
                visited.add(combination)
                for i in range(4):
                    nextCombClockwise = combination[:i] + str((int(combination[i]) + 1) % 10) + combination[i + 1:]
                    nextCombAntiClockwise = combination[:i] + str((int(combination[i]) + 9) % 10) + combination[i + 1:]
                    if nextCombClockwise not in deadends and nextCombClockwise not in visited:
                        nextTodo.add(nextCombClockwise)
                    if nextCombAntiClockwise not in deadends and nextCombAntiClockwise not in visited:
                        nextTodo.add(nextCombAntiClockwise)

            todo = nextTodo
            steps += 1

        return -1


print(Solution().openLock(deadends=["0201", "0101", "0102", "1212", "2002"], target="0202"))
print(Solution().openLock(deadends=["8888"], target="0009"))
print(Solution().openLock(deadends=["8887", "8889", "8878", "8898", "8788", "8988", "7888", "9888"], target="8888"))
