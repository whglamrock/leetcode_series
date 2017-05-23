
# Definition for a undirected graph node,
#   where the neighbors is a list of UndirectedGraphNodes

class UndirectedGraphNode(object):
      def __init__(self, x):

        self.label = x
        self.neighbors = []


# AC O(n) time/space solution, where n is the sum of number of neighbors of all nodes.
# However, the so called "UndirectedGraph" is not really undirected, because most likely
#   the 1->2, 2->1 pair will not appear twice in the BFS based on each
#   test case given by leetcode.

from collections import deque

class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):

        if not node:
            return

        newnode = UndirectedGraphNode(node.label)
        newlabeltonode = {node.label: newnode}
        queue = deque([node])

        while queue:
            oldnode = queue.popleft()
            # there is no need to check if oldnode is in the newlabeltonode dictionary
            for oldneighbor in oldnode.neighbors:
                if oldneighbor.label not in newlabeltonode:    # means this node haven't been visited/added to the queue
                    newlabeltonode[oldneighbor.label] = UndirectedGraphNode(oldneighbor.label)
                    queue.append(oldneighbor)    # BFS
                newlabeltonode[oldnode.label].neighbors.append(newlabeltonode[oldneighbor.label])

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

