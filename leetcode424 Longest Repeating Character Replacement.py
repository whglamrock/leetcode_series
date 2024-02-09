from collections import defaultdict

# maxCount = max(charCount.values()) can be replaced with maxCount = max(maxCount, charCount[char])
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        # the window that stores the count of each char
        charCount = defaultdict(int)
        maxLen = 0

        for r, char in enumerate(s):
            charCount[char] += 1
            maxCount = max(charCount.values())
            # keep in mind the s[l: r + 1] is not always valid.
            # 1) the idea is once we find a max size, we never shrink the size of the window again.
            # 2) if there is a bigger possible window, the s[l: r + 1] will become valid again.
            # 3) when r - l + 1 - maxCount <= k, it means the maxCount's corresponding char
            # will make s[l:r + 1] valid again, we don't move the left bound.
            if r - l + 1 - maxCount > k:
                charCount[s[l]] -= 1
                l += 1
            maxLen = max(maxLen, r - l + 1)

        return maxLen


print(Solution().characterReplacement('ABBAAAB', 2))


'''
# a even faster solution without repetitively looking for the max charCount in the window 
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        charCount = defaultdict(int)
        ans = 0
        maxCount = 0
        for r, char in enumerate(s):
            charCount[char] += 1
            maxCount = max(maxCount, charCount[char])
            if r - l + 1 - maxCount > k:
                charCount[s[l]] -= 1
                if not charCount[s[l]]:
                    del charCount[s[l]]
                l += 1
            ans = max(ans, r - l + 1)

        return ans
'''