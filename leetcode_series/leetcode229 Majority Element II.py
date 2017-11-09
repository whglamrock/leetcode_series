
# Majority Voting Algorithm idea from: https://gregable.com/2013/10/majority-vote-algorithm-find-majority.html
# O(n) time, O(1) space solution

class Solution(object):
    def majorityElement(self, nums):

        if (not nums):
            return []

        count1, count2, candidate1, candidate2 = 0, 0, 0, 1
        # the count1, count2 just need to be check if they are zero
        for num in nums:
            if num == candidate1:
                count1 += 1
            elif num == candidate2:
                count2 += 1
            elif count1 == 0:
                candidate1 = num
                count1 += 1
            elif count2 == 0:
                candidate2 = num
                count2 += 1
            # if num != candidate1/candidate2, both count1 and count2 needs to -1
            # e.g., [0,0,1,1,2], when num == 2, it needs to one 0 and one 1 to
            # keep the majority of 0 and 1. When count1 or count2 hits zero, it means
            # the corresponding candidate cannot keep its majority at this point.
            # However, if the replaced num occurs afterwards, the candidate can be assigned
            # to that value again.
            else:
                count1 -= 1
                count2 -= 1

        ans = []
        if nums.count(candidate1) > len(nums) / 3:
            ans.append(candidate1)
        if nums.count(candidate2) > len(nums) / 3:
            ans.append(candidate2)

        return ans



Sol = Solution()
nums = [2,3,0,0,0,0,1,1,1,1,1,1]
print(Sol.majorityElement(nums))