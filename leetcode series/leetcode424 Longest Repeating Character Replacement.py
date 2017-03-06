from collections import deque
class Solution(object):
    def characterReplacement(self, s, k):

        if (not s) or len(s) == 0:
            return 0
        if k >= len(s):
            return len(s)

        dic = {}
        for i in xrange(len(s)):
            if s[i] not in dic:
                dic[s[i]] = [i]
            else:
                dic[s[i]].append(i)

        for item in dic:
            if len(dic[item]) == 0:
                dic[item] = []
                continue
            interval = []
            for i in xrange(1, len(dic[item])):
                interval.append(dic[item][i] - dic[item][i - 1] - 1)
            dic[item] = interval

        def helper(nums, target):
            window = deque()
            cursum = 0
            longest = 0
            for i in xrange(len(nums)):
                while window and cursum + nums[i] > target:
                    cursum -= window[0]
                    window.popleft()
                window.append(nums[i])
                cursum += nums[i]
                longest = max(longest, len(window))
            return longest

        longest = 0
        for item in dic:
            if len(dic[item]) == 0:
                longest = max(longest, k + 1)
                continue
            maxcover = helper(dic[item], k)
            longest = max(longest, maxcover + k + 1)

        return min(longest, len(s))


Sol = Solution()
s = 'ABBAAAB'
print Sol.characterReplacement(s, 2)
