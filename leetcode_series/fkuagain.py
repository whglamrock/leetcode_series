
class Solution(object):
    def twoSum(self, nums, target):
        if not nums:
            return []

        dic = {}
        for i, num in enumerate(nums):
            print i, num
            if num not in dic:
                dic[num] = [i]
            else:
                dic[num].append(i)

        for num in nums:
            if target - num in dic:
                if target - num != num:
                    return [dic[num][0], dic[target - num][0]]
                else:
                    if len(dic[num]) > 1:
                        return dic[num][:2]
                    else:
                        continue

        return []


nums = [3, 5, 4, 5, 2, 3, 1, 7]
target = 10
Sol = Solution()
print Sol.twoSum(nums, target)





























































































































