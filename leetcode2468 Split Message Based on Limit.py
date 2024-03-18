from typing import List

class Solution:
    def splitMessage(self, message: str, limit: int) -> List[str]:
        # numOfParts is the number of parts
        numOfParts = 0
        # sumOfStringLengthOfIndexes is the total string length of all indexes appeared in all parts. e.g., blabla<12/13>'s index is 12
        sumOfStringLengthOfIndexes = 0

        # 1) 3 + len(str(numOfParts)) * 2 < limit is to make sure numOfParts is not too big and each split message
        # has at least non empty substring other than the <a/b>
        # 2) sumOfStringLengthOfIndexes + len(message) + (3 + len(str(numOfParts))) * numOfParts is the total length of split messages
        # 3) We need numOfParts to be as small as possible so we brute force it. But if certain numOfParts works,
        # it doesn't mean all bigger numOfParts will work ==> this means we can't binary search
        # 4) P.S., limit can >> message: in which case numOfParts will "+= 1" once, becoming 1 from 0.
        while 3 + len(str(numOfParts)) * 2 < limit and sumOfStringLengthOfIndexes + len(message) + (3 + len(str(numOfParts))) * numOfParts > limit * numOfParts:
            numOfParts += 1
            sumOfStringLengthOfIndexes += len(str(numOfParts))

        ans = []
        if 3 + len(str(numOfParts)) * 2 < limit:
            i = 0
            for j in range(1, numOfParts + 1):
                lengthOfSubstr = limit - (len(str(j)) + 3 + len(str(numOfParts)))
                ans.append('%s<%s/%s>' % (message[i:i + lengthOfSubstr], j, numOfParts))
                i += lengthOfSubstr

        return ans


print(Solution().splitMessage(message="this is really a very awesome message", limit=9))
print(Solution().splitMessage(message="short message", limit=15))
