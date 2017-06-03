
# O(m + n) time, O(1) space optimal solution

class Solution(object):
    def merge(self, nums1, m, nums2, n):

        # set each element from the biggest to smallest
        while m and n:
            if nums1[m - 1] <= nums2[n - 1]:
                nums1[m + n - 1] = nums2[n - 1]
                n -= 1
            else:
                nums1[m + n - 1] = nums1[m - 1]
                m -= 1

        while n:
            nums1[n - 1] = nums2[n - 1]
            n -= 1

        #return nums1   # stupid leetcode asks for returning nothing



a = [0,0,0,0,0,]
b = [1,2,3,4,5]
m = 0
n = 5
c = Solution()
d = c.merge(a, m, b, n)
print d




