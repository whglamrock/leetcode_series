
# idea: use prime numbers to build the key
# Two strings with different lengths can't have the same key: if that happens, then exists m and n (m != n)
#   where the product of m prime numbers == the product of n prime numbers, which is impossible.
#   So the prime number approach can keep each key unique

from collections import defaultdict

class Solution(object):
    def groupAnagrams(self, strs):

        primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101]
        def calculatekey(string):

            key = 1
            for letter in string:
                key *= primes[ord(letter) - ord('a')]

            return key

        dic = defaultdict(list)
        for string in strs:
            key = calculatekey(string)
            dic[key].append(string)

        ans = [value for value in dic.values()]
        return ans



Sol = Solution()
strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
print Sol.groupAnagrams(strs)
