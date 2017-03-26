
class Solution(object):
    def merge(self, nums1, m, nums2, n):

        if m == 0:
            for x in range(n):
                nums1[x]=nums2[x]
        else:
            i = 0
            j = 0
            while i<m+n and j<n:
                if nums1[i]>nums2[j]:
                    for k in range(m+n-2,i-1,-1):
                        nums1[k+1] = nums1[k]
                    nums1[i] = nums2[j]
                    j += 1
                    i += 1
                else:
                    i += 1
            if j<n:
                for l in range(m+j,m+n):
                    nums1[l] = nums2[l-m]



a = [0,0,0,0,0]
b = [1,2,3,4,5]
m = 0
n = 5
c = Solution()
d = c.merge(a,m,b,n)
print d




