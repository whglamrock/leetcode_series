
class LogSystem(object):

    def __init__(self):
        self.logs = []

    def put(self, id, timestamp):
        """
        :type id: int
        :type timestamp: str
        :rtype: None
        """
        self.logs.append([id, timestamp])


    def retrieve(self, s, e, gra):
        """
        :type s: str
        :type e: str
        :type gra: str
        :rtype: List[int]
        """
        # e.g., use "2017:01:01:23:59:59" to easily build mapping
        granularityToIndex = {'Year': 5, 'Month': 8, 'Day': 11, 'Hour': 14, 'Minute': 17, 'Second': 20}
        index = granularityToIndex[gra]

        start, end = s[:index], e[:index]
        ans = []

        for id, timestamp in self.logs:
            if start <= timestamp[:index] <= end:
                ans.append(id)

        return ans


        # Your LogSystem object will be instantiated and called as such:
        # obj = LogSystem()
        # obj.put(id,timestamp)
        # param_2 = obj.retrieve(s,e,gra)