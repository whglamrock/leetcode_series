from typing import List

class NumArray:
    def __init__(self, nums: List[int]):
        self.prefixSums = []
        for num in nums:
            if not self.prefixSums:
                self.prefixSums.append(num)
            else:
                self.prefixSums.append(num + self.prefixSums[-1])

    def sumRange(self, left: int, right: int) -> int:
        if left == 0:
            return self.prefixSums[right]
        else:
            return self.prefixSums[right] - self.prefixSums[left - 1]


nums = [-2, 0, 3, -5, 2, -1]
Sol = NumArray(nums)
print(Sol.sumRange(0, 5))


# Your NumArray object will be instantiated and called as such:
# numArray = NumArray(nums)
# numArray.sumRange(0, 1)
# numArray.sumRange(1, 2)
