# let's assume
# the length of input array is n,
# average length of Strings in nums is k,
# Then, compare 2 strings will take O(k).
# Sorting will take O(nlgn)
# Appending to StringBuilder takes O(n).
# So total Running Time will be O(nklgn) + O(n) = O(nklgn).
# Running Space is obvious: O(n), depending on the python sort

# key idea: for x, y in nums, compare string x+y and string y+x.
class Solution:
    def largestNumber(self, nums):

        nums = [str(x) for x in nums]
        # it means if y + x > x + y, then y should be the leading one
        nums.sort(cmp = lambda x, y: cmp(y + x, x + y))   # different from 'cmp = lambda y, x: cmp(y + x, x + y)'
        if nums[0] == '0':
            while len(nums) > 1 and nums[0] == '0':
                nums.pop(0)

        return ''.join(nums)

# P.S.: remember how to write the cmp sort function! Also the key = lambda sort...

Sol = Solution()
nums = [3, 30, 34, 5, 9]
print Sol.largestNumber(nums)