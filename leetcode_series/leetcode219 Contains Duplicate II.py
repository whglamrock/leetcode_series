
# for enumerate operator, see: https://docs.python.org/2/library/functions.html#enumerate

class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        
        dic = {}
        for i, v in enumerate(nums):
            if v in dic and i - dic[v] <= k: # if there exists: (current index of v)-(smallest index of v)<=k
                return True
            dic[v] = i # the dic[v] only store the closest index of nums[i] to the next equal
            # number nums[j]
        return False



a = [1,0,1,1]
Sol = Solution()
print Sol.containsNearbyDuplicate(a,1)



'''
class Solution(object):
    def containsNearbyDuplicate(self, nums, k):

        dick = {}
        for i in xrange(len(nums)):
            if nums[i] not in dick:
                dick[nums[i]] = {i}
            else:
                for index in dick[nums[i]]:
                    if abs(index - i) <= k:
                        return True
                dick[nums[i]].add(i)

        return False
'''


