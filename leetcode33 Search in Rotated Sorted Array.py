
# the simplest one pass solution.
# comparing the nums[mid] with nums[l] to divide the condition is easier than comparing nums[m] & target

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return -1

        l, r = 0, len(nums) - 1
        while l <= r:
            m = l + (r - l) / 2
            if nums[m] == target:
                return m
            # instead of comparing nums[m] & target, we divide the condition by whether the left half is ascending
            # Note: the nums[l] == nums[m] is for case like nums = [3, 1], target = 1
            elif nums[l] <= nums[m]:  # ascending from l to m
                if nums[l] <= target < nums[m]:
                    r = m - 1
                else:
                    l = m + 1
            else:  # ascending from m to r
                if nums[m] < target <= nums[r]:
                    l = m + 1
                else:
                    r = m - 1

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


