# pay attention to the data structure: binary index tree
# idea from: https://discuss.leetcode.com/topic/33747/148ms-python-solution-binary-indexed-tree/2

class NumArray(object):

    def __init__(self, nums):

        self.bit = [0] * (len(nums) + 1)
        self.nums = nums
        for i, num in enumerate(nums):
            k = i + 1
            while k < len(nums) + 1:
                self.bit[k] += num
                k += k & (-k)


    def update(self, i, val):

        diff = val - self.nums[i]
        self.nums[i] = val
        k = i + 1
        while k < len(self.nums) + 1:
            self.bit[k] += diff
            k += k & (-k)


    # sum[i,...j], inclusive.
    def sumRange(self, i, j):

        sumiminusone, sumj = 0, 0
        # notice that i don't need to ++ here. Because sum(0, i) includes nums[i],
        # sum(0, j) - sum(0, i) = sum(i + 1, j).
        j += 1
        while j > 0:
            sumj += self.bit[j]
            j -= j & (-j)
        # sum(0, i - 1)
        while i > 0:
            sumiminusone += self.bit[i]
            i -= i & (-i)

        return sumj - sumiminusone



# Your NumArray object will be instantiated and called as such:
# numArray = NumArray(nums)
# numArray.sumRange(0, 1)
# numArray.update(1, 10)
# numArray.sumRange(1, 2)