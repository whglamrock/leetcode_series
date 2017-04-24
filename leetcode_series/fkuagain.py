
class UndirectedGraphNode(object):
      def __init__(self, x):

        self.label = x
        self.neighbors = []


from collections import deque

class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):

        if not node:
            return

        # the newnode is the return value
        newnode = UndirectedGraphNode(node.label)
        newlabeltonode = {node.label: newnode}
        queue = deque([node])

        while queue:
            oldnode = queue.popleft()
            for neighbor in oldnode.neighbors:
                if neighbor.label not in newlabeltonode:
                    newlabeltonode[neighbor.label] = UndirectedGraphNode(neighbor.label)
                    queue.append(neighbor)
                newlabeltonode[oldnode.label].neighbors.append(newlabeltonode[neighbor.label])

        return newnode



Sol = Solution()
a = UndirectedGraphNode(0)
b = UndirectedGraphNode(1)
c = UndirectedGraphNode(5)
d = UndirectedGraphNode(2)
e = UndirectedGraphNode(3)
f = UndirectedGraphNode(4)
a.neighbors = [b, c]
b.neighbors = [a, c, d]
c.neighbors = [a, b, f, f, c]
d.neighbors = [b, e]
e.neighbors = [d, f, f]
f.neighbors = [c, c, e, e]
ans = Sol.cloneGraph(a)
print ans.label

for neighbor in ans.neighbors:
    print neighbor.label





























































































































