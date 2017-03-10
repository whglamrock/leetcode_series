class Solution(object):
    def fourSum(self, nums, target):

        def findNsum(nums, target, N, result, results):

            if len(nums) < N or N < 2 or target < nums[0] * N or target > nums[-1] * N:  # early termination
                return
            if N == 2: # two pointers solve sorted 2-sum problem
                l,r = 0,len(nums)-1
                while l < r:
                    s = nums[l] + nums[r]
                    if s == target:
                        results.append(result + [nums[l], nums[r]])
                        l += 1
                        while l < r and nums[l] == nums[l-1]:
                            l += 1
                    elif s < target:
                        l += 1
                    else:
                        r -= 1
            else: # recursively reduce N
                for i in xrange(len(nums)-N+1):
                    if i == 0 or (i > 0 and nums[i-1] != nums[i]):
                        findNsum(nums[i+1:], target-nums[i], N-1, result+[nums[i]], results)
                        # in the first round of the loop, for every nums[i], the goal becomes to find
                        # another N-1 items in nums that have a sum of target-nums[i], the results store
                        # the answers that needed to be returned; the result stores the elements to be
                        # based on (e.g. if we need 4sum that equal to 11, we've already had [-4,5], all we
                        # need to do is to find other two items that have as sum of 10 and the [-4,5] is to
                        # be based on in this seeking process.)

        results = []
        findNsum(sorted(nums), target, 4, [], results)
        return results


s = [0,1,5,0,1,5,5,-4]
target = 11
Sol = Solution()
print Sol.fourSum(s,target)


'''
class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        nums.sort()
        for i in xrange(len(nums)-3):
            for j in xrange(i+1, len(nums)-2):
                #if i > 0 and nums[i] == nums[i-1] and j > 0 and nums[j] == nums[j-1]:
                    #continue
                l, r = j+1, len(nums)-1
                while l < r:
                    s = nums[i] + nums[j] + nums[l] + nums[r]
                    if s < target:
                        l += 1
                    elif s > target:
                        r -= 1
                    else:
                        res.append([nums[i], nums[j], nums[l], nums[r]])
                        while l < r and nums[l] == nums[l+1]:
                            l += 1
                        while l < r and nums[r] == nums[r-1]:
                            r -= 1
                        l += 1; r -= 1

        def judge(ans1,ans2):
            for k in range(4):
                if ans1[k] != ans2[k]:
                    return False
            return True

        x = 0
        while x < len(res)-1:
            y = x+1
            while y < len(res):
                if judge(res[x],res[y]) == True:
                    del res[y]
                    continue
                y += 1
            x += 1

        return res
'''


