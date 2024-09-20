from random import randint
from copy import deepcopy
from typing import List


# idea from: https://discuss.leetcode.com/topic/53985/well-explained-o-n-java-solution-by-using-random-class-and-swapping-current-with-a-random-previous-index
class Solution:
    def __init__(self, nums: List[int]):
        self.nums = nums

    def reset(self) -> List[int]:
        return self.nums

    def shuffle(self) -> List[int]:
        ans = deepcopy(self.nums)
        for i in range(1, len(ans)):
            # randint is inclusive for both ends
            j = randint(0, i)
            ans[i], ans[j] = ans[j], ans[i]
        return ans


# Real interview experience from Uber Phone Screen:
'''
from copy import deepcopy
from random import randint, randrange
from typing import List
from collections import defaultdict


# Follow-up 1:
# nums = [1, 2, 3, 4]
# written by interviewer; need to decide whether this logic has any problem (P.S.: it's not gonna work).
# we can print out the test cases
def optional_shuffle(x):
    n = len(x)
    for i in range(n):
        j = randrange(n)
        x[i], x[j] = x[j], x[i]
    
    return x

# Problem statement: given an array x of length n, write code to shuffle the array. All possible permutations must be equally likely.
class Solution:
    def shuffle(self, nums: List[int]) -> List[int]:
        # i == 3
        # i == 4
        for i in range(1, len(nums)):
            # j will be in [0, 1, 2, 3]
            # 25%: j == 2 got swapped ==> nums = [1, 2, 4, 3, 5]
            # j will be in [0, 1, 2, 3, 4]
            # 80%: j not == index 2 (num == 4); total probability of 4 stays at index 2 is 25% * 0.8 = 20%
            j = randint(0, i)
            nums[i], nums[j] = nums[j], nums[i]
        
        return nums

# [1, 2, 3, 4], total # of permutations: 4 * 3 * 2 * 1 = 24
def generatePermutations() -> str:
    permutations = []
    nums = [1, 2, 3, 4]
    def dfs(currPermutation: List[int], currNums: List[int]):
        #print(currPermutation, currNums)
        if not currNums:
            permutations.append(currPermutation)
            return
        
        for i, num in enumerate(currNums):
            nextPermutation = currPermutation + [num]
            nextNums = currNums[:i] + currNums[i + 1:]
            dfs(nextPermutation, nextNums)
    
    dfs([], nums)
    ans = []
    for permutation in permutations:
        ans.append(','.join(str(num) for num in permutation))
    return ans

def serialize(permutation: List[int]) -> str:
    return ','.join(str(num) for num in permutation)
    
allPerms = generatePermutations()
sol = Solution()
shuffleCount = defaultdict(int)
for i in range(240000):
    serializedShuffle = serialize(sol.shuffle([1, 2, 3, 4]))
    #serializedShuffle = serialize(optional_shuffle([1, 2, 3, 4]))
    shuffleCount[serializedShuffle] += 1

print(shuffleCount)

# Follow-up 2:
# Generate a random m-element subset of the numbers less than n.
# O(n) time + O(n) space (need to generate the original nums array) for the shuffle method; for shuffled_nums[:m], O(m) time + O(m) space; overall O(n) time + O(n) space; 
# need to discuss how to optimize to O(m) space (or if it's even possible to optimize time)
'''