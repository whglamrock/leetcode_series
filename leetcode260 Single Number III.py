
# hash table: o(n) time complexity, o(logn) space complexity
# An interesting and delicate solution: https://leetcode.com/discuss/70790/easy-python-o-n-o-1-solution
# along with my comments.

class Solution(object):
    def singleNumber(self, nums):

        dick = {}
        ans = []
        for item in nums:
            if item not in dick:
                dick[item] = 1
            else:
                del dick[item]

        for item in dick:
            ans.append(item)

        return ans



Sol = Solution()
nums = [1, 2, 1, 3, 2, 5]
print Sol.singleNumber(nums)