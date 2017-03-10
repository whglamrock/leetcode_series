# Stupid question

class Solution(object):
    def countSegments(self, s):

        if not s: return 0

        count = 0
        for i, char in enumerate(s):
            if (i == 0 and char != ' ') or (i >= 1 and char != ' ' and s[i - 1] == ' '):
                count += 1

        return count



# or one liner: return len(s.split(''))
# when no parameter is chosen for Python split, it will skip all spaces
