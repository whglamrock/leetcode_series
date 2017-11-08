
class Vector2D(object):

    def __init__(self, vec2d):

        self.lst = []
        if (not vec2d):
            return
        for i in xrange(len(vec2d)):
            for j in xrange(len(vec2d[i])):
                self.lst.append(vec2d[i][j])
        self.lst.reverse()

    def next(self):

        if self.hasNext():
            return self.lst.pop()

    def hasNext(self):

        return len(self.lst) != 0



# Your Vector2D object will be instantiated and called as such:
# i, v = Vector2D(vec2d), []
# while i.hasNext(): v.append(i.next())