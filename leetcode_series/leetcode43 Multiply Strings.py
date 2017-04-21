
# idea came from: https://discuss.leetcode.com/topic/30508/easiest-java-solution-with-graph-explanation

class Solution(object):
    def multiply(self, num1, num2):

        if not num1 or not num2:
            return None

        # using example like "100 * 100", we can know at most how many digits the answer has
        digits = [0 for _ in xrange(len(num1) + len(num2))]

        for i, digit1 in enumerate(num1):
            for j, digit2 in enumerate(num2):
                product = (ord(digit1) - ord('0')) * (ord(digit2) - ord('0'))
                tens = product / 10
                ones = product % 10
                digits[i + j] += tens
                digits[i + j + 1] += ones

        res = 0
        for digit in digits:
            res = res * 10 + digit
        return str(res)



Sol = Solution()
num1 = '15'
num2 = '25'
print Sol.multiply(num1, num2)

