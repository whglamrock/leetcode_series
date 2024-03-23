from typing import List

# The idea is use index -> number mapping to form linked lists (mapping defines the "next" connection)
# e.g., nums = [2,1,3], starting from index 0, the linked lists are: 2(index 0) -> 3(index2) -> None &
# 1(index1) -> itself (circle)
# For the case when nums doesn't contain any duplicates, a linked list starting with index 0 and ending with n + 1
# will ALWAYS exist (although it's a bit tricky to prove, in real interview we just need to mention it).
# So in the case where exists duplicates and only 1 number is duplicated, the n + 1 must have been swapped with the
# duplicate number. Thus we will have a (multiple -> one) number to index mapping and the number at this index
# is the starting point of the cycle, and also the duplicate number. Then the question becomes lc142.
class Solution(object):
    def findDuplicate(self, nums: List[int]) -> int:

        if not nums or len(nums) == 1:
            return -1

        slow, fast = 0, 0
        while True:
            slow = nums[slow]
            fast = nums[fast]
            fast = nums[fast]
            if slow == fast:
                break

        # refer to lc142 to see floyd's algorithm.
        slow = 0
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]

        return slow


print(Solution().findDuplicate([3, 1, 2, 4, 4]))


# in real interview, if the O(1) extra space is needed, this becomes a hard level question (see lintcode 633)
# An explanation that may be helpful: https://leetcode.com/problems/find-the-duplicate-number/discuss/72846/My-easy-understood-solution-with-O(n)-time-and-O(1)-space-without-modifying-the-array.-With-clear-explanation./75491
