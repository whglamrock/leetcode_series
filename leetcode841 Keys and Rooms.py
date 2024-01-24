from typing import List

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = set()
        visited.add(0)
        todo = set(rooms[0])
        while todo:
            nextTodo = set()
            for key in todo:
                visited.add(key)
                for nextRoom in rooms[key]:
                    if nextRoom not in visited:
                        nextTodo.add(nextRoom)
            todo = nextTodo

        return len(visited) == len(rooms)
