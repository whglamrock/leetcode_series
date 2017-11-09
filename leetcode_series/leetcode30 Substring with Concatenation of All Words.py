
class Solution:

    def findSubstring(self, s, words):

        if len(words) == 0:
            return []
        # initialize d, l, ans
        l = len(words[0])
        d = {}      # store the words in dictionary, to more efficiently call them in the following code
        for w in words:
            if w in d:
                d[w] += 1   # a word may occur multiple times
            else:
                d[w] = 1

        ans = []

        # sliding window(s)
        for k in xrange(l): # only need to loop l times: in our case, the j travels respectively in:
            # 'foo bar bar foo...', 'oob arb arf ...', 'oba rba rfo ...', in l times we for sure can find the
            # substring match. e.g., if l == 3, there is no need to do k == 4 (j travels in: 'bar bar foo ...', which
            # is redundant cuz we've already had 'foo bar bar foo...')
            left = k
            subd = {}
            count = 0
            for j in xrange(k, len(s)-l+1, l):
                tword = s[j:j+l]

                # if it's a valid word
                if tword in d:
                    if tword in subd:   # store the substring in subd word by word, and count each word.
                        subd[tword] += 1
                    else:
                        subd[tword] = 1
                    count += 1  # count the number of words in subd to compare with len(words) (count != len(subd))

                    # when error: a single word occur more times than in the words
                    while subd[tword] > d[tword]: # strip the part before current tword one by one
                        subd[s[left:left+l]] -= 1
                        left += l
                        count -= 1
                        # e.g., in our case, the substring 'foobarbar' is not qualified, because
                        # subd[bar] = 2 > d[bar] = 1. At this moment, left still = 0, subd = {'foo':1,'bar':2}.
                        # The while loop does: subd[s[0:3]] = subd[foo] = 1-1 = 0, left = 0+3 = 3, count = 3-1 = 2;
                        # subd[s[3:6]] = subd[bar] = 2-1 = 1, left = 3+3 = 6, count = 2-1 = 1;
                        # then subd[bar] == d[bar] = 1 and we do next j loop, the subd = {'bar':1 }.
                        # In other test cases, the part before 'BAR'(1) differs but this while loop still works .
                    if count == len(words):
                        ans.append(left)

                # when not a valid word
                else:
                    left = j + l  # always keep the 'left' equal to next j cuz 'left' needs to add in 'ans'.
                    subd = {}  # clear the subd
                    count = 0

        return ans



Sol = Solution()
s = 'foobarbarfoothefoobarfooman'
# s = 'foobarBARfoothefoobarfooman'(1)
words = ["foo", "bar",'foo']
print Sol.findSubstring(s,words)

