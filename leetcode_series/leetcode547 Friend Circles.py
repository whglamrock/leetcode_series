
# typical union find solution

class Solution(object):
    def findCircleNum(self, M):

        if not M or not M[0]:
            return 0

        dic = {}
        unionid = 0
        n = len(M)
        for i in xrange(n):
            for j in xrange(i, n):
                if M[i][j] == 1:
                    if i not in dic and j not in dic:
                        dic[i] = unionid
                        dic[j] = unionid
                        unionid += 1
                    elif i in dic and j not in dic:
                        dic[j] = dic[i]
                    elif j in dic and i not in dic:
                        dic[i] = dic[j]
                    else:
                        previd = dic[i]
                        currid = dic[j]
                        if previd == currid: continue
                        for key in dic:
                            if dic[key] == previd:
                                dic[key] = currid

        ansset = set()
        for value in dic.values():
            ansset.add(value)
        return len(ansset)
