'''
stupid leetcode very unfriendly to iterative solution.
if not replacing the list 'item' with string, it will get MLE.
'''
class Solution(object):
    def numberOfPatterns(self, m, n):

        keyboard = [[1,2,3], [4,5,6], [7,8,9]]
        position = {1:[0,0], 2:[0,1], 3:[0,2], 4:[1,0], 5:[1,1], 6:[1,2], 7:[2,0], 8:[2,1], 9:[2,2]}
        route = {1:{2,4,5,6,8},3:{2,5,6,4,8},7:{4,5,8,2,6},9:{5,6,8,2,4},2:{1,3,4,5,6,7,9},4:{1,2,5,7,8,3,9},6:{2,3,5,8,9,1,7},8:{4,5,6,7,9,1,3},5:{1,2,3,4,6,7,8,9}}

        def check(already, alreadydict, next):
            return str(keyboard[(position[int(already[-2])][0] + position[next][0])/2][(position[int(already[-2])][1] + position[next][1])/2]) in alreadydict

        res = [9]
        prev = [str(i) + '-' for i in xrange(1,10)]
        for j in xrange(n - 1):
            new = []
            for item in prev:
                dick = set(item.split('-'))
                for num in xrange(1, 10):
                    if str(num) not in dick:
                        if num in route[int(item[-2])]:
                            new.append(item + str(num) + '-')
                        else:
                            if check(item, dick, num) == True:
                                new.append(item+str(num) + '-')
            res.append(len(new))
            prev = new

        return sum(res[m - 1:])


Sol = Solution()
print Sol.numberOfPatterns(1,9)
