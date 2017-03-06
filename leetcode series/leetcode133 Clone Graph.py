# Definition for a undirected graph node
class UndirectedGraphNode(object):
      def __init__(self, x):
        self.label = x
        self.neighbors = []

# AC O(n) time/space solution, not very efficient though...
class Solution(object):
    def cloneGraph(self, node):

        if (not node):
            return

        dick = {}
        nodelist = {}   # to visit the newly cloned nodes.
        savelist = {}   # to visit the actual node in the original graph
        todo = [node]
        while todo:
            new = todo.pop()
            if new.label not in nodelist:
                newnode = UndirectedGraphNode(new.label)
                nodelist[new.label] = newnode
                savelist[new.label] = new
            for item in new.neighbors:
                if item.label not in nodelist:
                    todo.append(item)

        for item in savelist:
            dick[item] = []
            for neighbor in savelist[item].neighbors:
                dick[item].append(neighbor.label)

        new = nodelist[node.label]
        todo = [new]
        ans = new
        while todo:    # clone the graph by stack
            cur = todo.pop()
            if cur.label not in dick: continue
            for val in dick[cur.label]:
                cur.neighbors.append(nodelist[val])
            del dick[cur.label]
            for item in cur.neighbors:
                if item.label in dick:
                    todo.append(item)

        return ans


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

