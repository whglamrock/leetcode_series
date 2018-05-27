
class Solution(object):

    def isBipartite(self, graph):
        n = len(graph)
        colors = [-1] * n

        for node in xrange(n):
            # the reason to call isValidColor multiple times is because the graph might be disconnected:
            # e.g. if we directly do: "return self.isValidColor(graph, colors, 0, 0)", it will fail to pass with
            #   test case: [[],[2,4,6],[1,4,8,9],[7,8],[1,2,8,9],[6,9],[1,5,7,8,9],[3,6,9],[2,3,4,6,9],[2,4,5,6,7,8]]
        	if colors[node] == -1 and not self.isValidColor(graph, colors, 0, node):
        		return False
        return True

    # DFS with the color check
    # color is the color we are gonna paint node with
    def isValidColor(self, graph, colors, color, node):
    	if colors[node] != -1:
    		return colors[node] == color
    	colors[node] = color
    	for neighbor in graph[node]:
    		# paint all neighbors with different color
    		if not self.isValidColor(graph, colors, 1 - color, neighbor):
    			return False
    	return True