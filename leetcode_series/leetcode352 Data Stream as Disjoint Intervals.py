
from heapq import *

class Interval(object):
    def __init__(self, s=0, e=0):

        self.start = s
        self.end = e


class SummaryRanges(object):

    def __init__(self):

        self.intervals = []

    # heap is the min heap
    def addNum(self, val):

        heappush(self.intervals, (val, Interval(val, val)))

    def getIntervals(self):

        stack = []

        while self.intervals:
            curr, currinterval = heappop(self.intervals)
            if stack and curr <= stack[-1][1].end + 1:
                last, lastinterval = stack.pop()
                lastinterval.end = max(lastinterval.end, currinterval.end)
                stack.append((last, lastinterval))
            else:
                stack.append((curr, currinterval))

        self.intervals = stack
        return [x[1] for x in stack]




'''
# naive BST solution will get TLE because of extreme case like [1, 2, 3, ... 1999, 2000]

class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e


class TreeNode(object):
    def __init__(self, val):

        self.val = val
        self.left = None
        self.right = None


class SummaryRanges(object):

    def __init__(self):

        self.root = None


    def addNum(self, val):

        if not self.root:
            self.root = TreeNode(val)
            return
        cur = self.root
        prev = cur
        while cur:
            prev = cur
            if cur.val > val:
                cur = cur.left
            elif cur.val < val:
                cur = cur.right
            else:
                return
        newnode = TreeNode(val)
        if prev.val > val:
            prev.left = newnode
        else:
            prev.right = newnode
        #print val


    # do the inorder traversal
    def getIntervals(self):

        cur = self.root
        stack = []
        ans = []

        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            ans.append(cur.val)
            cur = cur.right

        res = []
        if not ans:
            return []
        s, e = ans[0], None
        for i in xrange(len(ans)):
            if i == 0:
                e = ans[0]
            else:
                if ans[i] > e + 1:
                    res.append(Interval(s, e))
                    s, e = ans[i], ans[i]
                else:
                    e += 1
        res.append([s, e])
        return res
'''