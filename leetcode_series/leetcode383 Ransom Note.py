
# super easy, but using 'import collections, collections.Counter(magazine) is more high level'

class Solution(object):
    def canConstruct(self, ransomNote, magazine):

        dick1 = {}
        dick2 = {}

        for item in ransomNote:
            if item not in dick1:
                dick1[item] = 1
            else:
                dick1[item] += 1

        for item in magazine:
            if item not in dick2:
                dick2[item] = 1
            else:
                dick2[item] += 1

        for item in dick1:
            if item not in dick2:
                return False
            if dick1[item] > dick2[item]:
                return False

        return True