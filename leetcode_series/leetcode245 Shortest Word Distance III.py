
class Solution(object):
    def shortestWordDistance(self, words, word1, word2):

        dick = {}
        for i in xrange(len(words)):
            if words[i] not in dick:
                dick[words[i]] = [i]
            else:
                dick[words[i]].append(i)

        def findshortest1(lst):
            lst.sort()
            min = lst[1]-lst[0]
            for i in xrange(len(lst)-1):
                if lst[i+1]-lst[i] < min:
                    min = lst[i+1]-lst[i]
            return min


        def findshortest2(lst1, lst2):
            min = abs(lst1[0] - lst2[0])
            for i in lst1:
                for j in lst2:
                    if abs(i-j) < min:
                        min = abs(i-j)
            return min

        if word1 != word2:
            return findshortest2(dick[word1], dick[word2])
        else:
            return findshortest1(dick[word1])



words = ["practice", "makes", "perfect", "coding", "makes"]
word1 = 'makes'
word2 = 'makes'
Sol = Solution()
print Sol.shortestWordDistance(words,word1,word2)
