# use hash-table to build O(n) solution
class Solution(object):
    def twoSum(self, nums, target):

        dic = {}
        for i in xrange(len(nums)):
            if nums[i] not in dic:
                dic[nums[i]] = [i]
            else:
                dic[nums[i]].append(i)

        for item in dic:
            if target - item in dic:
                if target - item != item:
                    return [dic[item][0], dic[target - item][0]]
                else:
                    if len(dic[item]) > 1:
                        return [dic[item][0], dic[item][1]]


'''
# in lintcode, several edge cases need to be considered.
class Solution:

    def twoSum(self, nums, target):
        # write your code here
        if (not nums): return []

        dick = {}
        for i in xrange(len(nums)):
            if nums[i] not in dick:
                dick[nums[i]] = [i]
            else:
                dick[nums[i]].append(i)

        ans = []
        for num in dick:
            if target - num in dick:
                if target - num == num:
                    if num == 0 and len(dick[num]) == 1:   # this doesn't but double 0s work
                        continue
                    elif len(dick[num]) > 1:  # if len(dick[num]) == 1, we can't choose num
                        ans.append(dick[num][0])
                        ans.append(dick[num][1])
                elif target - num != num:    # normal case
                    ans.append(dick[num][0])
                    ans.append(dick[target-num][0])
                break

        ans.sort()
        return ans
'''
