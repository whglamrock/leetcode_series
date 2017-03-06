# O(1) time complexity, because num can't be bigger than 9.
class Solution(object):
    def readBinaryWatch(self, num):

        num = min(num, 9)
        hrpool = [1, 2, 4, 8]
        minpool = [1, 2, 4, 8, 16, 32]

        hrs, mins = {0: {0}}, {0: {0}}
        for i in xrange(1, num + 1):
            hrs[i] = set()
            mins[i] = set()
            for item in hrs[i - 1]:
                for hrnum in hrpool:
                    if hrnum <= item:
                        continue
                    if item + hrnum < 12:
                        hrs[i].add(item + hrnum)
            for item in mins[i - 1]:
                for minnum in minpool:
                    if minnum <= item:
                        continue
                    if item + minnum < 60:
                        mins[i].add(item + minnum)

        ans = set()
        for i in xrange(num + 1):
            for hour in hrs[i]:
                for minute in mins[num - i]:
                    hour = str(hour)
                    if minute < 10:
                        minute = '0' + str(minute)
                    else:
                        minute = str(minute)
                    ans.add(hour + ':' + minute)

        return list(ans)