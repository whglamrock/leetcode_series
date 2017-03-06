# use each frequency as a 'bucket', within which stores the corresponding elements.
# retrieve them one by one from the maximum, with k -= 1 every time.
class Solution(object):
    def topKFrequent(self, nums, k):

        dick = {}
        maximum = 0
        for num in nums:
            if num not in dick:
                dick[num] = 1
            else:
                dick[num] += 1
            if dick[num] > maximum:
                maximum = dick[num]

        frequency = [[] for i in xrange(maximum+1)]
        for item in dick:
            frequency[dick[item]].append(item)

        res = []
        for i in xrange(len(frequency)-1,-1,-1):
            if frequency[i]:
                for item in frequency[i]:
                    res.append(item)
                    k -= 1
                    if k == 0:
                        return res


k = 4
nums = [1,1,4,6,7,14,5,1,2,6,8,9,1,8,8,8,10,1,1,2,1,1,1,2,1,2,2,1,1,]
Sol = Solution()
print Sol.topKFrequent(nums,k)

