
class Solution(object):
    def findMissingRanges(self, A, lower, upper):

        result = []
        A.append(upper+1)
        pre = lower-1

        for i in A:
           if (i == pre+2):    # there is only one value between 'pre' and 'pre+2'
               result.append(str(i-1))
           elif (i > pre+2):    # need to add a 'A->B' range to the result
               result.append(str(pre+1)+"->"+str(i-1))
           pre = i    # the 'pre' records the previously visited value

        return result
