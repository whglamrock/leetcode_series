
from collections import deque

class Solution(object):
    def myAtoi(self, string):
        """
        :type string: str
        :rtype: int
        """
        if not string:
            return 0

        queue = deque()
        i = 0

        # find the first non whitespace char
        while i < len(string) and string[i] == ' ':
            i += 1
        # if it's a sign, add to the queue
        if i < len(string) and string[i] in '+-':
            queue.append(string[i])
            i += 1

        # return 0 for the invalid case
        if i >= len(string) or not string[i].isdigit():
            return 0

        # add all the valid digits
        while i < len(string) and string[i].isdigit():
            queue.append(string[i])
            i += 1

        ans = 0
        flag = 1
        if queue[0] in '+-':
            sign = queue.popleft()
            if sign == '-':
                flag = -1
        while queue:
            ans = ans * 10 + int(queue.popleft())
        ans = flag * ans
        return min(max(ans, -2147483648), 2147483647)



print Solution().myAtoi('   -42')
print Solution().myAtoi('4193 with words')
print Solution().myAtoi('words and 987')
print Solution().myAtoi('-91283472332')

