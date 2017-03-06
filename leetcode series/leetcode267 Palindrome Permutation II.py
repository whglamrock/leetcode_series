from copy import copy
class Solution(object):
    def generatePalindromes(self, s):

        dick = {}
        for char in s:
            if char not in dick:
                dick[char] = 1
            else:
                dick[char] += 1

        odd = []
        for item in dick:
            if dick[item] % 2 != 0:
                odd.append(item)

        todo = []
        if len(odd) > 1: return []
        if odd:
            newpool = copy(dick)
            newpool[odd[0]] -= 1
            if newpool[odd[0]] == 0:
                del newpool[odd[0]]
            todo.append((odd[0], newpool))
        else:
            for item in dick:
                newpool = copy(dick)
                newpool[item] -= 2
                if newpool[item] == 0:
                    del newpool[item]
                todo.append((item + item, newpool))

        ans = []
        while todo:
            next = []
            for already, pool in todo:
                for candidate in pool:
                    nextpool = copy(pool)
                    if nextpool[candidate] == 2:
                        del nextpool[candidate]
                    else:
                        nextpool[candidate] -= 2
                    next.append((candidate + already + candidate, nextpool))
            if (not next):
                ans = todo
                break
            todo = next

        for i in xrange(len(ans)):
            ans[i] = ans[i][0]

        return ans


Sol = Solution()
s = 'aaaabb'
print Sol.generatePalindromes(s)
