
# Definition for a Node.

class Node(object):
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors



from collections import deque

# leetcode OJ is so fucking stupid that the order of each node's neighbor has to be identical to the original

class Solution(object):
    def cloneGraph(self, root):
        """
        :type node: Node
        :rtype: Node
        """
        if not root:
            return None

        res = Node(root.val, [])
        nodeToCopy = {root: res}
        q = deque()
        q.append(root)

        while q:
            node = q.popleft()
            nodeCopy = nodeToCopy[node]
            for neighbor in node.neighbors:
                if neighbor not in nodeToCopy:
                    neighborCopy = Node(neighbor.val, [])
                    nodeToCopy[neighbor] = neighborCopy
                    q.append(neighbor)
                else:
                    neighborCopy = nodeToCopy[neighbor]
                nodeCopy.neighbors.append(neighborCopy)

        return res


