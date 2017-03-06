'''
The trick is: if a number n%9 == 0, addDigits(num) = 9; if not, addDigits(num) = num%9.
Idea came from: https://leetcode.com/discuss/52795/o-1-solution-with-mod-operation
'''
class Solution(object):

    def addDigits(self, num):
        if num==0:
            return 0
        return num%9 if num%9!=0 else 9

Sol = Solution()
print Sol.addDigits(10)

'''
class Solution(object):
    def addDigits(self, num):

        def newdigits(nums):
            lst = []
            while nums>0:
                lst.append(nums%10)
                nums = (nums-nums%10)/10
            return sum(lst)

        while num/10>0:
            num = newdigits(num)

        return num
'''
