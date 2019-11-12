
class Solution(object):
    def judgePoint24(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)
        if n == 1 and abs(nums[0] - 24) < 0.0001:
            return True

        for i in xrange(n):
            for j in xrange(n):
                if i == j:
                    continue
                tmp = []
                for k in xrange(n):
                    if k == i or k == j:
                        continue
                    tmp.append(nums[k])
                if self.judgePoint24(tmp + [nums[i] + nums[j]]):
                    return True
                if self.judgePoint24(tmp + [nums[i] - nums[j]]):
                    return True
                if self.judgePoint24(tmp + [nums[j] - nums[i]]):
                    return True
                if self.judgePoint24(tmp + [nums[i] * nums[j]]):
                    return True
                if nums[i] != 0 and self.judgePoint24(tmp + [nums[j] / float(nums[i])]):
                    return True
                if nums[j] != 0 and self.judgePoint24(tmp + [nums[i] / float(nums[j])]):
                    return True

        return False



print Solution().judgePoint24([4, 1, 8, 7])
print Solution().judgePoint24([1, 1, 2, 3])