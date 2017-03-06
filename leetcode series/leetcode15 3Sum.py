'''
The key idea is to lock the left integer num[i] and find two numbers on its right that add up to
-num[i]
'''

class Solution(object):
    def threeSum(self, nums):

        if not nums or len(nums) < 3: return []
        ans = []
        nums.sort()
        n = len(nums)

        for i in xrange(n - 2):
            if i > 0 and nums[i] == nums[i - 1]: continue
            l, r = i + 1, n - 1
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                if s < 0:
                    l += 1
                elif s > 0:
                    r -= 1
                else:
                    ans.append([nums[i], nums[l], nums[r]])
                    while l < r and nums[l] == nums[l + 1]:
                        l += 1
                    while l < r and nums[r] == nums[r - 1]:
                        r -= 1
                    # put the following here then they won't affect the above while loops
                    l += 1
                    r -= 1

        return ans



s = [0,0,0]
target = 0
Sol = Solution()
print Sol.threeSum(s)










