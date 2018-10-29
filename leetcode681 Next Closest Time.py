
class Solution(object):
    def nextClosestTime(self, time):

        h1, m1 = time.split(':')
        digits = [h1[0], m1[0], h1[1], m1[1]]
        h1, m1 = int(h1), int(m1)
        # all possible digit combinations (each digit is presented in String)
        combinations = self.getCombinations(digits, [[]])

        ans = ''
        minDiff = 2147483547
        for a, b, c, d in combinations:
            h2, m2 = int(a + b), int(c + d)
            # filter out invalid cases
            if h2 > 24 or m2 >= 60:
                continue
            if h2 == h1 and m2 == m1:
                continue
            timeDiff = self.getTimeDiff(h1, m1, h2, m2)
            if minDiff > timeDiff:
                minDiff = timeDiff
                # need to consider the singe digit hour and minute
                h2Str = str(h2) if h2 >= 10 else '0' + str(h2)
                m2Str = str(m2) if m2 >= 10 else '0' + str(m2)
                ans = h2Str + ':' + m2Str

        # need to consider the case when time's 4 digits are same (leetcode is a fucking idiot!)
        return ans if ans else time

    def getCombinations(self, digits, current):
        if len(current[0]) == 4:
            return current
        next = []
        for digit in digits:
            for combination in current:
                next.append(combination + [digit])
        return self.getCombinations(digits, next)

    # get the time2 - time1 in minutes (always positive)
    def getTimeDiff(self, h1, m1, h2, m2):
        hDiff = h2 - h1
        if hDiff < 0:
            hDiff += 24
        mDiff = m2 - m1
        if mDiff < 0:
            hDiff -= 1
            mDiff += 60
            if hDiff < 0:
                hDiff += 24

        return hDiff * 60 + mDiff



Sol = Solution()
print Sol.nextClosestTime('19:34')
print Sol.nextClosestTime('00:00')
print Sol.nextClosestTime('23:29')



