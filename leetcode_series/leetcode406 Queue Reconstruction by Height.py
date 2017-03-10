# idea from: https://discuss.leetcode.com/topic/60394/easy-concept-with-python-c-java-solution
class Solution(object):
    def reconstructQueue(self, people):

        people.sort(key = lambda x: (x[0], -x[1]))
        people.reverse()
        print people
        ans = []
        for item in people:
            ans.insert(item[1], item)
            print ans

        return ans


Sol = Solution()
people = [[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]
Sol.reconstructQueue(people)

