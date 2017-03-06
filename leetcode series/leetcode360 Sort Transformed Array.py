'''
Many very troublesome corner cases, but the following solution is o(n) time complexity.
'''
class Solution(object):
    def sortTransformedArray(self, nums, a, b, c):
        if (not nums):
            return

        def f(x):
            return a*(x**2)+b*x+c

        ans = []
        if a == 0:
            if b>=0:
                for num in nums:
                    ans.append(f(num))
            else:
                for i in xrange(len(nums)-1,-1,-1):
                    ans.append(f(nums[i]))
            return ans

        mid = -float(b)/float(2*a)
        for index in xrange(len(nums)):
            if nums[index] >= mid:
                break

        if a > 0:
            if index > 0:
                i, j = index-1, index
                while i>=0 and j<len(nums):
                    if f(nums[i]) >= f(nums[j]):
                        ans.append(f(nums[j]))
                        j += 1
                    else:
                        ans.append(f(nums[i]))
                        i -= 1
                if i>=0:
                    for k in xrange(i,-1,-1):
                        ans.append(f(nums[k]))
                else:
                    for l in xrange(j, len(nums)):
                        ans.append(f(nums[l]))
            else:
                for num in nums:
                    ans.append(f(num))
        else:
            i, j = 0, len(nums)-1
            while i<index and j>= index:
                if f(nums[i]) >= f(nums[j]):
                    ans.append(f(nums[j]))
                    j -= 1
                else:
                    ans.append(f(nums[i]))
                    i += 1
            if i == index:
                for k in xrange(j, index-1, -1):
                    ans.append(f(nums[k]))
            else:
                for l in xrange(i, index):
                    ans.append(f(nums[l]))

        return ans