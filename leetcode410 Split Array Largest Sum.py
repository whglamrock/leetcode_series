
# O(N * log(N)) binary search solution

class Solution(object):
    def splitArray(self, nums, m):

        # judge if we can divide array into m continuous subArrays that the sum of each <= mid.
        def valid(mid):

            count, curr = 0, 0
            for num in nums:
                curr += num
                if curr > mid:
                    count += 1
                    # curr should not be set zero here, because we exclude num from this round of sum
                    curr = num
                    # it's False even when count == m because we excluded num from this round of sum
                    if count >= m:
                        return False

            return True

        l, r = max(nums), sum(nums)
        while l < r:
            mid = l + (r - l) / 2
            # if mid is valid, then the optimal value <= this mid.
            if valid(mid):
                r = mid
            # the optimal value can't be this mid
            else:
                l = mid + 1

        return l
        # or return r. Based on the exit condition of while loop, l can only == r.