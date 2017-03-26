
# see explanation: https://discuss.leetcode.com/topic/33770/short-simple-o-n-log-n

class Solution(object):
    def countRangeSum(self, nums, lower, upper):

        prefixsum = [0]
        for num in nums:
            prefixsum.append(prefixsum[-1] + num)

        def sort(lo, hi):

            mid = (lo + hi) / 2
            if mid == lo:
                return 0
            # the start/end of the sum range both in either left or right half
            count = sort(lo, mid) + sort(mid, hi)
            i, j = mid, mid
            # then we need to look at the case when start is in left half, end is in right half
            for left in prefixsum[lo:mid]:
                # we need prefixsum[i] - left >= lower, so in the below case, exclude i
                while i < hi and prefixsum[i] - left < lower:
                    i += 1  # all indices less than the final i doesn't satisfy
                # j++ because we want j is one more than the index that satisfies the <= upper
                # requirement so j - i will be right equal to the increased count
                while j < hi and prefixsum[j] - left <= upper:
                    j += 1  # all indices bigger than the final j doesn't satisfy
                count += j - i
            # actually, the left half and right half are already sorted, we just need to merge
            # and the python Timsort can do the merge in linear time (e.g., a lazy way here)...

            # the prefixsum[lo:hi].sort() doesn't work here!
            prefixsum[lo:hi] = sorted(prefixsum[lo:hi])
            return count

        return sort(0, len(prefixsum))