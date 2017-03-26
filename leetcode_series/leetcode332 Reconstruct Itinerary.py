
# Important Euler path theory: http://www.ctl.ua.edu/math103/euler/howcanwe.htm
# Euler Path search algorithm: http://stackoverflow.com/questions/17467228/looking-for-algorithm-finding-euler-path

# see solution explanation: https://discuss.leetcode.com/topic/36370/short-ruby-python-java-c
# in the explanation, the process of retreat (build path backward) goes like (in following steps
# the '*' means the vertex is confirmed, every '->' eliminates one edge from trips dictionary):
#   JFK -> A -> C -> D -> A (stuck, A has no more destinations, so A will be the current last);
#   JFK -> A -> C -> D -> A* (check if D has more destinations);
#   JFK -> A -> C -> D -> B -> C -> JFK -> D -> A* (add another sub path inside again and again until
#     D has no more destinations, and the order of path addition is in lexicographical order);
#   JFK -> A -> C -> D -> B -> C -> JFK -> D* -> A*;
#   ... (since in the above path, no vertex has more destinations, so after few more checks),
#   JFK* -> A* -> C* -> D* -> B* -> C* -> JFK* -> D* -> A*.

# An delicate recursive solution, O(n) space; except the sort part, the rest takes O(n) time.

from collections import defaultdict
class Solution(object):
    def findItinerary(self, tickets):

        trips = defaultdict(list)
        # sort in lexicographic order
        tickets.sort()
        tickets.reverse()
        for a, b in tickets:
            trips[a].append(b)

        ans = []
        def visit(airport):
            while trips[airport]:
                visit(trips[airport].pop())
            ans.append(airport)

        visit('JFK')
        return ans[::-1]



tickets = [["JFK","A"],["A","C"],["C","D"],["D","A"],["JFK","D"],["D","B"],["B","C"],["C","JFK"]]
Sol = Solution()
print Sol.findItinerary(tickets)

