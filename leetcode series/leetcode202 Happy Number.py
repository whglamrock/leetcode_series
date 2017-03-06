'''
Unhappy numbers will enter into a infinite loop; happy numbers will end up with 1 as the sum of digit squares.
'''
class Solution(object):
    def isHappy(self, n):

        unhappylist = [4, 16, 37, 58, 89, 145, 42, 20] #unhappy cycle(see problem description about "loop")
        if n in unhappylist:
            return False
        else:
            current = n
            while (current not in unhappylist) and current != 1:
                digits= []
                while current > 0:
                    digits.append(current%10)
                    current = (current-(current%10))/10
                for item in digits:
                    current += item*item
            if current in unhappylist:
                return False
            else:
                return True

Sol = Solution()
print Sol.isHappy(19)

