
# elegant iterative solution, perfectly using the backtracking idea

class Solution(object):
    def subsets(self, nums):

        res = [[]]
        nums.sort()

        for num in nums:
            # in this way, the "bound for for loop is changed" error won't occur
            res += [item + [num] for item in res]
            # or simply do, next = deepcopy(res), for item in res: next.append(item + [num]), res = next

        return res



nums = [1,2,3,4]
Sol = Solution()
ans = Sol.subsets(nums)
print ans



'''
# classic recursive DFS solution

class Solution(object):
    def subsets(self, nums):

        if not nums:
            return []

        nums.sort()
        self.nums = nums
        self.res = []
        self.dfs(0, [])

        return self.res

    def dfs(self, i, path):

        self.res.append(path)
        for j in xrange(i, len(self.nums)):
            self.dfs(j + 1, path + [self.nums[j]])
'''