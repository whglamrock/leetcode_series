
# no need to use memo.
# simply try every option, because whether the DFS word depends on every single step(recursion).

class Solution(object):
    def countArrangement(self, N):

        self.count = 0

        def helper(N, index, nums):
            if index > N:
                self.count += 1
                return

            for i, num in enumerate(nums):
                # no need to use memo to prune because of the following if condition
                if num % index == 0 or index % num == 0:
                    helper(N, index + 1, nums[:i] + nums[i + 1:])

        helper(N, 1, range(1, N + 1))
        return self.count

