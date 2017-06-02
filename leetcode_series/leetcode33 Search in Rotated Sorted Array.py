
# the simplest one pass solution came from lc 88.

class Solution(object):
    def search(self, nums, target):

        if not nums:
            return -1

        l, r = 0, len(nums)-1
        # remember in this rotated array, always use the left element to compare with the mid;
            #   you have to consider more cases if using the right element

        while l <= r:
            mid = (l + r) / 2
            if nums[mid] == target:
                return mid
            # for the nums[l] == nums[mid] case, consider test case like:
            #   nums = [3, 1], target = 1
            #   nums = [5, 1, 2, 3, 4], target = 1  (at last, nums[5, 1])
            #   nums == [2, 3, 4, 5, 1], target == 1  (at last, nums[5, 1])
            elif nums[l] <= nums[mid]:  # when there are more (or exactly half) elements on the left
                if nums[l] <= target < nums[mid]:  # monotonously increasing
                    r = mid - 1
                else:   # target < nums[l] or target > nums[mid]
                    l = mid + 1
            else:  # when there are more elements on the right of the pivot
                if nums[mid] < target <= nums[r]:  # monotonously increasing
                    l = mid + 1
                else:
                    r = mid - 1

        # P.S., if nums == [5, 1], and the "elif" condition is nums[l] < nums[mid], the while loop will go
        #   into the small else condition of big else condition; at this point, l == r - 1 == mid, s
        #   letting r = mid - 1 will miss the right search range and return -1

        return -1



nums = [4, 5, 6, 7, 3]
target = 3
Sol = Solution()
print Sol.search(nums, target)



'''
# a delicate two pass O(logN) solution by finding the smallest element first

class Solution(object):

    def search(self, nums, target):

        if not nums:
            return -1
        n = len(nums)

        l, r = 0, n - 1

        # find the index of smallest element
        # the exit condition is l == r
        while l < r:
            mid = l + (r - l) / 2
            if nums[mid] > nums[r]:
                l = mid + 1
            else:   # nums[mid] < nums[r], then nums[r] is still the candidate
                r = mid

        pivot = l
        l, r = 0, n - 1

        # using another "realmid" instead of the mid.
        # in each search, we don't choose the actual mid element to compare;
        #   we choose an element (it's just like we are using another standard to choose)
        #   on the "right" of mid by pivot elements.
        while l <= r:
            mid = l + (r - l) / 2
            realmid = (mid + pivot) % n  # n, not n - 1, because realmid can n - 1
            if nums[realmid] == target:
                return realmid
            # the recalculation of l and r will still be based on the mid:
            elif nums[realmid] < target:
                l = mid + 1
            else:
                r = mid - 1

        return -1
'''


