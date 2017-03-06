# By the definition of ugly number, if its factors include any numbers other than 2,3,5 (e.g. -2, -3, -5, etc.), it
# is not a ugly number.
class Solution(object):
    def isUgly(self, num):

        for p in [2,3,5]:
            while num%p == 0 < num: # instead of 'num%p == 0 and num>0', this judgement statement is faster
                num /= p # divide the num by 2,3,5 ('yin shi fen jie') to see if there are other factors left.

        return num == 1


Sol = Solution()
print Sol.isUgly(214748364)



