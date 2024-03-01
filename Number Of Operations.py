# Questions:
# nums - positive integers - of size n
# queries - positive integers - of size m
# for queries[i], make all elements of nums equal to queries[i]
# allowed operation for any number of times: increase or decrease an element of nums by 1
# return an answer array of length m, ans[i] denotes the minimum # operation to make all nums equal to queries[i]

# Time complexity: O(m * log(n) + n * log(n))
class NumOfOperations:
    def findLastIndexSmallerThanOrEqualToNum(self, nums, target):
        if not nums:
            return -1
        if nums[0] > target:
            return -1
        if nums[-1] <= target:
            return len(nums) - 1

        l, r = 0, len(nums) - 1
        m = -1

        while l <= r:
            m = (l + r + 1) // 2
            if nums[m] > target:
                r = m - 1
            else:
                l = m

            if l == r:
                return -1 if nums[l] > target else l

        return m

    def numOfOperations(self, nums, queries):
        nums.sort()
        numsSum = self.accumulationSum(nums)

        ans = []
        for target in queries:
            indexSmallerOrEqual = self.findLastIndexSmallerThanOrEqualToNum(nums, target)

            if indexSmallerOrEqual != -1:
                numOfOperationsSmallerOrEqual = target * (indexSmallerOrEqual + 1) - numsSum[indexSmallerOrEqual]
                numOfOperationsBigger = (numsSum[-1] - numsSum[indexSmallerOrEqual]) - target * (
                            len(nums) - indexSmallerOrEqual - 1)
                ans.append(numOfOperationsSmallerOrEqual + numOfOperationsBigger)
            else:
                ans.append(numsSum[-1] - target * len(nums))

        return ans

    # return the sum of nums[:i]
    def accumulationSum(self, nums):
        numsSum = []
        accumulatedSum = 0
        for num in nums:
            accumulatedSum += num
            numsSum.append(accumulatedSum)

        return numsSum


sol = NumOfOperations()
print(sol.numOfOperations([8, 1, 2, 3], [7, 8]))


nums = [47, 50, 97, 58, 87, 72, 41, 63, 41, 51, 17, 21, 7, 100, 69, 66, 79, 92, 84, 9, 57, 26, 26, 28, 83, 38]
queries = [50, 84, 76, 41, 64, 82, 20, 22, 64, 7, 38, 92, 39, 28, 22, 3, 41, 46, 47, 50, 88, 51, 9, 49, 38, 67, 26, 65,
           89, 27, 71, 25, 77, 72, 65, 41, 84, 68, 51, 26, 84, 24, 79, 41, 96, 83, 92, 9, 93, 84, 35, 70, 74, 79, 37,
           38, 26, 26, 41, 26]
expected = [607, 855, 747, 655, 633, 825, 943, 905, 633, 1227, 685, 1009, 675, 805, 905, 1331, 655, 625, 619, 607, 929,
            605, 1179, 611, 685, 653, 833, 639, 949, 819, 689, 851, 759, 699, 639, 655, 855, 661, 605, 833, 855, 869,
            783, 655, 1097, 839, 1009, 1179, 1031, 855, 721, 679, 723, 783, 697, 685, 833, 833, 655, 833]

for i, a in enumerate(sol.numOfOperations(nums, queries)):
    if a != expected[i]:
        print(i, a, expected[i])
