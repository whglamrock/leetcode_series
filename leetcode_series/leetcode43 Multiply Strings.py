# idea came from: https://discuss.leetcode.com/topic/30508/easiest-java-solution-with-graph-explanation
class Solution(object):
    def multiply(self, num1, num2):

        anslst = [[] for i in xrange(len(num1)+len(num2))]
        for i in xrange(len(num1)):
            for j in xrange(len(num2)):
                product = (ord(num1[i])-48)*(ord(num2[j])-48)
                tens = product/10
                unit = product%10
                anslst[i+j].append(tens)
                anslst[i+j+1].append(unit)

        ans = 0
        for item in anslst:
            ans = ans*10+sum(item)

        return str(ans)

