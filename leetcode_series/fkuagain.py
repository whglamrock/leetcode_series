
from Queue import *
q = PriorityQueue()
a = [1,2,3,4]
b = [4,3,2,1]
c = 0
projects = sorted(zip(a, b), key = lambda x: x[1])
print projects
j = 0
for i in xrange(10):
    while j < len(projects):
        if projects[j][1] > 2:
            break
        else:
            q.put((-projects[j][0], projects[j][0]))
        j += 1
    if q.empty():
        break
    else:
        c += q.get()[1]

print c





























































































































