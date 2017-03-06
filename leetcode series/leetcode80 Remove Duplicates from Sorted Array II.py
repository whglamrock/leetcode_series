# super easy
class Solution(object):
    def removeDuplicates(self, nums):

        counter,i = 1, 1
        while i < len(nums):
            if nums[i] == nums[i-1]:
                counter += 1
            else:
                counter = 1
            if counter == 3:
                del nums[i]
                counter -= 1    # to deal with situation like [1,1,1,1]...
                continue
            i += 1