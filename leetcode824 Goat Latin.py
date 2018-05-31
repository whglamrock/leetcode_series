
class Solution(object):
    def toGoatLatin(self, S):

        vowel = ['a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U']
        S = S.split(" ")  # make it a list

        for i in xrange(len(S)):
            if S[i][0] in vowel:
                S[i] = S[i] + 'ma' + 'a' * (i + 1)
            else:
                S[i] = S[i][1:] + S[i][0] + 'ma' + 'a' * (i + 1)

        return ' '.join(S)



S = "I speak Goat Latin"
Sol = Solution()
print Sol.toGoatLatin(S)
