# I don't know what's the point of this question?
class Solution(object):
    def fizzBuzz(self, n):

        if (not n):
            return []

        ans = []
        for i in xrange(1, n + 1):
            if i % 15 == 0:
                ans.append('FizzBuzz')
            elif i % 3 == 0:
                ans.append('Fizz')
            elif i % 5 == 0:
                ans.append('Buzz')
            else:
                ans.append(str(i))

        return ans

