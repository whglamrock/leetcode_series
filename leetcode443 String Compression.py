
class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        l, r = 0, 0
        currUpdated = 0
        ans = 0
        while r < len(chars):
            # step 1: count the occurence of chars[l]
            while r < len(chars) and chars[r] == chars[l]:
                r += 1
            count = r - l
            # step 2: update chars & currUpdated pointer
            countStr = str(count)
            ans += 1    # add the length of a single char
            if count > 1:
                ans += len(countStr)
                for j in xrange(len(countStr)):
                    currUpdated += 1
                    chars[currUpdated] = countStr[j]
            currUpdated += 1    # move the currUpdated to the new char
            if r < len(chars):
                chars[currUpdated] = chars[r]
            l = r

        return ans


chars=["a","a","b","b","1","1","1","c","c","c","c","c"]
ans = Solution().compress(chars)
print ans
print chars[:ans]




