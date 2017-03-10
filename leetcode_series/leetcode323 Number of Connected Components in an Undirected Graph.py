# typical unionfind solution, strictly O(N) time/space
class Solution(object):
    def countComponents(self, n, edges):

        if not edges:
            return n

        self.unionid = 0
        uniondic = {}
        dic = {}

        def unionfind(a, b):
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
                if ida == idb: return
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

        #print uniondic
        return len(uniondic) + n - len(dic)


Sol = Solution()
n = 5
edges = [[0, 1], [1, 2], [3, 4]]
print Sol.countComponents(n, edges)










