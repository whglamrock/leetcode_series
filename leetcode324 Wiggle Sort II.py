
import random
class Solution(object):

    # find Kth largest element from leetcode215
    def findKthLargest(self, nums, k):  # O(n) time, O(1) space

        def exchange(a, i, j):
            a[i], a[j] = a[j], a[i]

        def partition(a, lo, hi):
            i, j = lo+1, hi
            while True:
                while i < hi and a[i] <= a[lo]:
                    i += 1
                while j > lo and a[j] >= a[lo]:
                    j -= 1
                if i >= j:
                    break
                exchange(a, i, j)
            exchange(a, lo, j)
            return j    # ensure the elements on the left/right of j are smaller/bigger

        def shuffle(a):
            for ind in xrange(1, len(a)):
                r = random.randrange(ind+1)
                exchange(a, ind, r)

        shuffle(nums)
        k = len(nums) - k   # find (len(nums)-k)th smallest element
        lo, hi = 0, len(nums)-1
        while lo < hi:
            j = partition(nums, lo, hi)  # every time the partition is called, the nums is changed.
            if j < k:
                lo = j + 1  # logarithmically reduce the search range.
            elif j > k:
                hi = j - 1
            else:
                break

        return nums[k]

    # idea from: https://discuss.leetcode.com/topic/41464/step-by-step-explanation-of-index-mapping-in-java
    def wiggleSort(self, nums):

        def newIndex(index, n):
            return (1 + 2*index) % (n | 1)  # remap to the 'virtual index'

        median = self.findKthLargest(nums, (len(nums)+1)/2)
        n = len(nums)
        left, right, i = 0, n-1, 0

        while i <= right:   # when i+right == n-1, exit the loop
            if nums[newIndex(i, n)] > median:
                swap1 = newIndex(left, n)
                swap2 = newIndex(i, n)
                nums[swap1], nums[swap2] = nums[swap2], nums[swap1]
                left += 1
                i += 1
            elif nums[newIndex(i, n)] < median:
                swap1 = newIndex(right, n)
                swap2 = newIndex(i, n)
                nums[swap1], nums[swap2] = nums[swap2], nums[swap1]
                right -= 1  # don't "i+=1" here, because i increase from 0.
                # or we can let i decrease from n-1 and add it to this "<median" condition,
                # then move "i+=1" from the ">median" condition
            else:   # can't increase the left, the increment only for ">median".
                i += 1

        # the reason why the 'i+=1' only exists for ">median" condition:
        # 1) i always <= right
        # 2) when i increases from 0 (in the above case), the left always <= i.
        # 3) newIndex(left, n) will always be odd, and newIndex(right, n) will always be even.
        # 4) when swapping nums[newIndex(left, n)], nums[newIndex(i, n)], these two are
           # actually both >= median... so left and i can increase at the same time.
        # 5) the above 4) doesn't work for nums[newIndex(right, n)]. after swapping with
           # nums[newIndex(right, n)], the new nums[newIndex(i, n)] could >, =, < median, which all needs
           # further action before i increases.

        #return nums    # the stupid leetcode asks to return nothing.



Sol = Solution()
nums = [13, 6, 5, 5, 4, 2]
print Sol.wiggleSort(nums)
