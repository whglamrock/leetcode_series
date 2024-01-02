from collections import defaultdict
from typing import List

class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        numOf1BitToNums = defaultdict(list)
        for num in arr:
            numOf1Bit = self.getNumber1Bit(num)
            numOf1BitToNums[numOf1Bit].append(num)

        numOf1Bits = sorted(numOf1BitToNums.keys())
        i = 0
        for numOf1Bit in numOf1Bits:
            nums = sorted(numOf1BitToNums[numOf1Bit])
            for num in nums:
                arr[i] = num
                i += 1
        return arr

    def getNumber1Bit(self, num: int) -> int:
        numOf1Bit = 0
        while num:
            numOf1Bit += int(num % 2)
            num //= 2
        return numOf1Bit


'''
# simpler solution using bit_count():
class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        arr.sort(key = lambda x: (x.bit_count(), x))
        return arr
'''