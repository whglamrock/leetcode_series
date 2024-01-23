from typing import List

# it's ok to use brute force, i.e., O(volume * N) time complexity. Idea come from: https://leetcode.com/problems/pour-water/solutions/171104/share-my-java-straightforward-and-concise-solution/
class Solution:
    def pourWater(self, heights: List[int], volume: int, k: int) -> List[int]:
        n = len(heights)
        i = k
        # for first 2 while loop we have to use ">=" not ">" or "<"
        for _ in range(volume):
            while i > 0 and heights[i] >= heights[i - 1]:
                i -= 1
            while i < n - 1 and heights[i] >= heights[i + 1]:
                i += 1
            while i > k and heights[i] == heights[i - 1]:
                i -= 1
            heights[i] += 1

        return heights
