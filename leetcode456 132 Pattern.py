
# idea: using stack to store the candidate value for s2, and traverse to find the s1
#   such that s1 < s2 > s3 (s3 > s1)
# P.S.: the maximum candidate for s3 is always the recently popped number from the stack

class Solution(object):
    def find132pattern(self, nums):

        if not nums or len(nums) < 3:
            return False

        s3 = -2147483648
        stack = []

        # traverse the nums, the pointers points to s1
        for i in xrange(len(nums) - 1, -1, -1):
            # remember this, so we don't need to check the relationship of s1, s2, s3
            if nums[i] < s3:
                return True
            # then this nums[i] >= s3
            # notice the while condition here, ">" instead of ">="
            while stack and stack[-1] < nums[i]:
                s3 = stack.pop()
            stack.append(nums[i])

        return False