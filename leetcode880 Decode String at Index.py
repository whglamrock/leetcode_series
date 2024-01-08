
# a lot of edge cases to cover. O(N) time solution
class Solution:
    def decodeAtIndex(self, s: str, k: int) -> str:
        currLen = 0
        # find the index whose corresponding length is just bigger or equal than k
        for i, char in enumerate(s):
            if char.isdigit():
                currLen *= int(char)
            else:
                currLen += 1
            if k <= currLen:
                break

        # start from the above index and scan shorten the string 1 char by 1 char
        for j in range(i, -1, -1):
            char = s[j]
            if char.isdigit():
                currLen /= int(char)
                k %= currLen
            else:
                # have to consider edge case where k == currLen * someInteger but k < the length at j + 1
                if k == currLen or k == 0:
                    return char
                currLen -= 1


print(Solution().decodeAtIndex(s="leet2code3", k=10))
print(Solution().decodeAtIndex(s="ha22", k=5))
print(Solution().decodeAtIndex(s="a2345678999999999999999", k=1))
print(Solution().decodeAtIndex(s="a2345678999999999999999", k=1))
print(Solution().decodeAtIndex(s="leet2code3", k=29))
print(Solution().decodeAtIndex(s="a232", k=11))
print(Solution().decodeAtIndex(s="vk6u5xhq9v", k=554))
