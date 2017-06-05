
# see explanation from: https://discuss.leetcode.com/topic/4661/c-solution-and-explanation/2

# for each unique number, we either choose or not choose it to put in each res's instance
#   so for a series of n duplicates, we can choose put 1 ~ n of them in each res's instance.

class Solution(object):
    def subsetsWithDup(self, nums):

        res = [[]]
        nums.sort()

        i = 0
        while i < len(nums):
            # count how many duplicates in a row
            count = 0
            while i + count < len(nums) and nums[count + i] == nums[i]:
                count += 1
            # for each individual added instance, use nums[i] to form a series a new instances;
            #   there are (count) nums[i] in total
            for j in xrange(len(res)):
                instance = res[j]
                for k in xrange(count):
                    # P.S. we have to build a newinstance, simply using instance.append(nums[i])
                    #   will result in appending a bunch of same instances into the res!
                    #   e.g., nums = [1,2,2], nums[i] = 2, count = 2, the res will be added
                    #   two [1,2,2] because the "Python append(x)" doesn't do deepcopy of x
                    newinstance = instance + [nums[i]]
                    res.append(newinstance)
                    instance = newinstance
            i += count

        return res



Sol = Solution()
S = [1,2,2,3,4]
print Sol.subsetsWithDup(S)



'''
# no extra space optimal solution
# can take [1,2,2,3] as an example to see how the range of j is changed

class Solution(object):
    def subsetsWithDup(self, nums):

        res = [[]]
        nums.sort()
        l = len(res)

        for i, num in enumerate(nums):
            if i == 0 or num != nums[i - 1]:
                l = len(res)    # the length of previous res
            # In the previous loop, every instance of the previous-previous res is added a
            #   nums[i - 1] to form a new instance in the previous res; there are in total
            #   len(previous-previous res) elements that have been added nums[i - 1];
            # to avoid adding the nums[i] to those elements again, we need to use len(res) - l
            #   as the start index of j:
            #   a) if nums[i] == nums[i - 1], the l will not be updated by the above if statement
            #   b) if nums[i] != nums[i - 1], the l will be updated to len(previous res) so
            #      len(previous len) - len(previous len) == 0 and j starts from 0
            for j in xrange(len(res) - l, len(res)):    # P.S. the range of j will not change
                res.append(res[j] + [num])

        return res
'''