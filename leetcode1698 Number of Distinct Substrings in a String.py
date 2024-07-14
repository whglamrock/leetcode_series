
# the algorithm described in: https://leetcode.com/problems/number-of-distinct-substrings-in-a-string/solutions/1010936/python-suffix-array-lcp-o-n-logn/
# is absolutely crazy and unnecessary in real interview. If you get asked to solve this question in O(nlogn) you can
# tell the interviewer to go fuck himself.
class Solution:
    def countDistinct(self, s: str) -> int:
        substrs = set()
        for i in range(len(s)):
            for j in range(i + 1, len(s) + 1):
                substr = s[i:j]
                substrs.add(substr)

        return len(substrs)
