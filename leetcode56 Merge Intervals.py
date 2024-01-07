from typing import List

# There is no way you can do better than O(N * log(N))
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        ans = []
        for l, r in intervals:
            if ans and l <= ans[-1][1]:
                ans[-1][1] = max(ans[-1][1], r)
                continue
            ans.append([l, r])

        return ans


print(Solution().merge([[1, 3], [2, 6], [8, 10], [15, 18]]))
print(Solution().merge([[5, 10], [1, 3]]))
