
# using 110101010111000 as an example: scanning from right to left,
# you should only flip if you accumulated a consecutive number of 1s or 0s.
class Solution:
    def minFlips(self, target: str) -> int:
        numOfFlips = 0
        curr = target[-1]
        for i in range(len(target) - 1, -1, -1):
            if target[i] != curr:
                numOfFlips += 1
                curr = target[i]
        # 1. for something like 000111000, the leading zeros don't need the one last flip
        # 2. for regular target like 110011, the left most block of 1s is not covered in the above for loop
        # 3. same idea as 2), this covers case like 11111
        if curr == '1':
            numOfFlips += 1

        return numOfFlips


print(Solution().minFlips("10111"))
print(Solution().minFlips("110101010111000"))
print(Solution().minFlips("0000"))
print(Solution().minFlips("11111"))
