from collections import defaultdict
from typing import List


# Definition for Employee
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates


class Solution:
    def __init__(self):
        self.ans = 0
        self.employeeIdToImportance = {}
        self.employeeToSubordinates = defaultdict(set)

    def getImportance(self, employees: List['Employee'], id: int) -> int:
        self.employeeToSubordinates = defaultdict(set)
        self.employeeIdToImportance = {}
        for employee in employees:
            self.employeeIdToImportance[employee.id] = employee.importance
            for subordinate in employee.subordinates:
                self.employeeToSubordinates[employee.id].add(subordinate)

        if id not in self.employeeIdToImportance:
            return 0
        if id not in self.employeeToSubordinates:
            return self.employeeIdToImportance[id]

        self.ans = 0
        self.dfs(id)
        return self.ans

    def dfs(self, currEmployeeId: int):
        self.ans += self.employeeIdToImportance[currEmployeeId]
        for subordinate in self.employeeToSubordinates[currEmployeeId]:
            self.dfs(subordinate)
