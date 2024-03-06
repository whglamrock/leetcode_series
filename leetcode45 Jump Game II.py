from typing import List

# implicit BFS idea:
# 1) At nums[0] you have to jump. say the farthest you can jump is currEnd (0 + nums[0]), then for all i values within
# [0, currEnd], you keep updating the currFarthest (which means the optimal farthest you can reach from the 2nd jump)
# 2) Once i == currEnd, you need to reset the currEnd to the currFarthest and increment the number of jumps
# 3) You don't need to scan all the way to i == len(nums) - 1 (because you already stand at the last position you don't
# need to further increment the number of jumps). It's also guaranteed from the problem description you can reach the end.
class Solution:
    def jump(self, nums: List[int]) -> int:
        numOfJumps = 0
        currEnd = 0
        currFarthest = 0
        for i in range(len(nums) - 1):
            currFarthest = max(currFarthest, i + nums[i])
            if i == currEnd:
                numOfJumps += 1
                currEnd = currFarthest

        return numOfJumps
