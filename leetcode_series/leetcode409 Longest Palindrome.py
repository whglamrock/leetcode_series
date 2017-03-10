class Solution(object):
    def longestPalindrome(self, s):

        letterpool = {}
        for letter in s:
            if letter not in letterpool:
                letterpool[letter] = 1
            else:
                letterpool[letter] += 1

        odd = 0
        even = 0
        for item in letterpool:
            if letterpool[item] % 2 == 0:
                even += letterpool[item]
            else:
                if odd == 0:
                    odd += letterpool[item]
                else:
                    odd += letterpool[item] - 1

        return odd + even



Sol = Solution()
s = 'asdfasdXcasfdasdfadasqee'
print Sol.longestPalindrome(s)
