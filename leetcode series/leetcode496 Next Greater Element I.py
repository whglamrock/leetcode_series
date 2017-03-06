
# O(n) idea from: https://discuss.leetcode.com/topic/77916/java-10-lines-linear-time-complexity-o-n-with-explanation
# The key is to find a decreasing subsequence

class Solution(object):
    def nextGreaterElement(self, nums1, nums2):

        ans = []
        stack = []
        dic = {}

        for i, num in enumerate(nums2):
            if i > 0 and num > nums2[i - 1]:
                while stack and stack[-1] < num:
                    previousnum = stack.pop()
                    dic[previousnum] = num
            stack.append(num)

        for num in nums1:
            if num not in dic:
                ans.append(-1)
            else:
                ans.append(dic[num])

        return ans