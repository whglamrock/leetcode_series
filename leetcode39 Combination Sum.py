
# remember the standard format of backtracking solution:

class Solution(object):
    def combinationSum(self, candidates, target):

        combis = []
        candidates.sort()
        pool = set(candidates)
        todo = [(target, 0, [])]
        if target in pool:
            combis.append([target])
        while todo:
            rest, i, combi = todo.pop()
            if rest < candidates[i]:
                continue
            if rest in pool and rest != target:
                combis.append(combi+[rest])
            while i < len(candidates) and rest >= candidates[i]:
                todo.append((rest-candidates[i], i, combi+[candidates[i]]))
                i += 1

        return combis



Sol = Solution()
candidates = [2,3,4,5,6,7]
target = 18
print Sol.combinationSum(candidates,target)
