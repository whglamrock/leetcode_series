
# google also has super easy OA questions...lol

class Solution(object):
    def findTheDifference(self, s, t):

        if len(t) == 0:
            return ''

        dicks = {}
        dickt = {}

        for item in s:
            if item not in dicks:
                dicks[item] = 1
            else:
                dicks[item] += 1

        for item in t:
            if item not in dickt:
                dickt[item] = 1
            else:
                dickt[item] += 1

        for item in dickt:
            if item not in dicks or dickt[item] > dicks[item]:
                return item

        return