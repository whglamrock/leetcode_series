# write down the binary representation from 1 to 32, we could find the regulation.
class Solution(object):
    def countBits(self, num):

        origin = [1]
        i = 1
        accum = 1
        ans = [1]
        while accum < num:
            add = []
            for item in origin:
                add.append(item+1)
            ans += origin+add
            origin += add
            i *= 2
            accum += i

        return [0]+ans[:num]

Sol = Solution()
print Sol.countBits(5)
