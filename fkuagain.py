
from heapq import *

pq = []
pq.append([-1, "fku"])
pq.append([-3, "suckme"])
pq.append([-2, "fkurself"])
pq.append([-2, "fuckurself"])
pq.sort(key=lambda x: (-x[0], x[1]))

while pq:
    count, sentence = pq.pop()
    print -count, sentence




























































