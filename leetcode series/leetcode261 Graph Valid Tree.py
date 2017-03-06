# Typical unionfind solution
class Solution(object):
    def validTree(self, n, edges):

        if not edges: return n == 1

        self.unionid = 0
        dic = {}
        uniondic = {}
        self.flag = True

        def unionfind(a, b):
            #print dic, uniondic
            if a not in dic and b not in dic:
                dic[a] = self.unionid
                dic[b] = self.unionid
                uniondic[self.unionid] = {a, b}
                self.unionid += 1
            elif a in dic and b not in dic:
                id = dic[a]
                dic[b] = id
                uniondic[id].add(b)
            elif b in dic and a not in dic:
                id = dic[b]
                dic[a] = id
                uniondic[id].add(a)
            else:
                ida = dic[a]
                idb = dic[b]
                if ida == idb: self.flag = False
                # in the following process, every elment will be unioned at most once,
                # so the time complexity is still O(N)
                if len(uniondic[ida]) > len(uniondic[idb]):
                    for item in uniondic[idb]:
                        uniondic[ida].add(item)
                        dic[item] = ida
                    del uniondic[idb]
                else:
                    for item in uniondic[ida]:
                        uniondic[idb].add(item)
                        dic[item] = idb
                    del uniondic[ida]

        for edge in edges:
            a, b = edge
            unionfind(a, b)
            # if there is a cycle, means all elements in the cycle is already deleted in uniondic
            # to avoid unnecessary key error, we directly return False here
            if not self.flag: return False

        if len(uniondic) != 1: return False   # not connected
        if len(dic) != n: return False    # there are nodes connected by no edges
        return True

