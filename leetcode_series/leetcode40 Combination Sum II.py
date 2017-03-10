# backtracking, idea came from lc 39, which I did it myself.
class Solution(object):
    def combinationSum2(self, candidates, target):

        combis = []
        candidates.sort()

        todo = [(target, 0, [])]
        while todo:
            rest, i, combi = todo.pop()
            if rest == 0:
                combis.append(combi)
            if i < len(candidates) and rest < candidates[i]:
                continue

            already = {}    # use it to make sure every newly added candidates[i] after combi[-1] is unique
            # e.g., candidates = [1,1,2,2,2,5,6], combi = [1,2] we only need to add each of 2,5,6 once to make new
            # combi: [1,2,2], [1,2,5], [1,2,6], and there should be only one [1,2,2]. And the case of
            # new combi = [1,2,2,2] will be executed in one of the incoming big while loops when combi = [1,2,2].
            while i < len(candidates) and rest >= candidates[i]:
                if candidates[i] not in already:
                    already[candidates[i]] = 1
                    todo.append((rest-candidates[i], i+1, combi+[candidates[i]]))
                i += 1

        return combis

Sol = Solution()
candidates = [1,1,2,2,2,2,5,6,7]
target = 10
print Sol.combinationSum2(candidates,target)