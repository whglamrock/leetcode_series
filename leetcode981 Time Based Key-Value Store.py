
from collections import defaultdict

class TimeMap(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        # map of map(string to list of int)
        self.keyToTimeToValue = defaultdict(dict)
        self.keyToTimes = defaultdict(list)

    def set(self, key, value, timestamp):
        """
        :type key: str
        :type value: str
        :type timestamp: int
        :rtype: None
        """
        self.keyToTimeToValue[key][timestamp] = value
        self.keyToTimes[key].append(timestamp)

    # find the biggest previous timestamp <= timestamp
    def get(self, key, timestamp):
        """
        :type key: str
        :type timestamp: int
        :rtype: str
        """
        # binary search
        times = self.keyToTimes[key]
        l, r = 0, len(times)

        while l < r:
            m = l + (r - l) / 2
            # m is not candidate
            if times[m] > timestamp:
                r = m
            # m is candidate
            else:
                if l == m:
                    break
                l = m

        if times[l] <= timestamp:
            return self.keyToTimeToValue[key][times[l]]
        else:
            return ''



tm = TimeMap()
tm.set('love', 'high', 10)
tm.set('love', 'low', 20)
print tm.get('love', 5)
print tm.get('love', 10)
print tm.get('love', 15)
print tm.get('love', 20)
print tm.get('love', 25)