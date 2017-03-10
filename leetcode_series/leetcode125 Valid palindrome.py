class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        i = 0
        j = 0
        while i+j < len(s):
            while (ord(s[i])<48) or (57<ord(s[i])<65) or (90<ord(s[i])<97) or (ord(s[i])>122):
                if i == len(s)-1:
                    return True
                i+=1
            while (ord(s[len(s)-j-1]))<48 or (57<ord(s[len(s)-j-1])<65) or (90<ord(s[len(s)-j-1])<97) or (ord(s[len(s)-j-1])>122):
                if j == len(s)-1:
                    return True
                j+=1

            if s[i]!= s[len(s)-j-1]:
                if ord(s[len(s)-j-1]) in range(97,123):
                    if ord(s[i]) in range(65,91):
                        if abs(ord(s[len(s)-j-1])-ord(s[i])) == 32:
                            return True
                        else:
                            return False
                    else:
                        return False
                elif ord(s[len(s)-j-1]) in range(65,91):
                    if ord(s[i]) in range(97,123):
                        if abs(ord(s[len(s)-j-1])-ord(s[i])) == 32:
                            return True
                        else:
                            return False
                    else:
                        return False
                else:
                    return False

            i+=1
            j+=1

        return True

a = Solution()
b = 'WGlGl'
print a.isPalindrome(b)

