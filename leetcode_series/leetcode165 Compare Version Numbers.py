
class Solution(object):
    def compareVersion(self, version1, version2):

        v1 = version1.split('.')
        v2 = version2.split('.')
        for i in range(min(len(v1),len(v2))):
            if int(v1[i])>int(v2[i]):
                return 1
            elif int(v1[i])<int(v2[i]):
                return -1
            else:
                continue

        if len(v1) == len(v2):
            return 0
        else:
            if len(v1)>len(v2):
                for j in range(i+1, len(v1)):
                    if int(v1[j]) != 0:
                        return 1
            else:
                for j in range(i+1, len(v2)):
                    if int(v2[j]) != 0:
                        return -1

        return 0



a = '10'
b = '10.0'
Sol = Solution()
print Sol.compareVersion(a,b)


