
from heapq import *

# 2 heap, O(N * K) solution that works in real interview but got TLE for stupid leetcode

class Solution(object):
    def medianSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[float]
        """

        smaller, bigger = [], []
        ans = []

        for i, num in enumerate(nums):
            # need to remove i - k. O(k) time
            if i >= k:
                sizeOfSmaller = len(smaller)
                for smallerNum, index in smaller:
                    if index == i - k:
                        smaller.remove((smallerNum, index))
                        break
                # the i - k was not in smaller
                if sizeOfSmaller == len(smaller):
                    for biggerNum, index in bigger:
                        if index == i - k:
                            bigger.remove((biggerNum, index))
                            break

            # need to re-heapify. O(K) time
            heapify(smaller)
            heapify(bigger)

            # push num to the heaps. O(logK) time
            heappush(bigger, (num, i))
            smallestOfBigger, j = heappop(bigger)
            heappush(smaller, (-smallestOfBigger, j))

            # balance the size; we always make sure smaller's size is 1 more bigger or equal to bigger's size
            while len(bigger) > len(smaller):
                smallestOfBigger, j = heappop(bigger)
                heappush(smaller, (-smallestOfBigger, j))
            while len(smaller) > len(bigger) + 1:
                biggestOfSmaller, j = heappop(smaller)
                biggestOfSmaller = -biggestOfSmaller
                heappush(bigger, (biggestOfSmaller, j))

            if i >= k - 1:
                # get the median
                if len(smaller) == len(bigger):
                    ans.append((-smaller[0][0] + bigger[0][0]) / 2.0)
                else:
                    ans.append(-smaller[0][0])

        return ans



print Solution().medianSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 3)



'''
// O(N * K) java solution that utilizes priorityQueue's remove by element value method (O(K) time)

public class Solution {
    PriorityQueue<Integer> minHeap = new PriorityQueue<Integer>();
    PriorityQueue<Integer> maxHeap = new PriorityQueue<Integer>(
        new Comparator<Integer>() {
            public int compare(Integer i1, Integer i2) {
                return i2.compareTo(i1);
            }
        }
    );
	
    public double[] medianSlidingWindow(int[] nums, int k) {
        int n = nums.length - k + 1;
        if (n <= 0) return new double[0];
            double[] result = new double[n];
            for (int i = 0; i <= nums.length; i++) {
                if (i >= k) {
                    result[i - k] = getMedian();
                    remove(nums[i - k]);
                }
                if (i < nums.length) {
                    add(nums[i]);
                }
            }
        return result;
    }
    
    // takes care of balancing as well
    private void add(int num) {
        if (num < getMedian()) {
            maxHeap.add(num);
        } else {
	        minHeap.add(num);
        }
        if (maxHeap.size() > minHeap.size()) {
                minHeap.add(maxHeap.poll());
        }
        if (minHeap.size() - maxHeap.size() > 1) {
            maxHeap.add(minHeap.poll());
        }
    }
	
    private void remove(int num) {
        if (num < getMedian()) {
            maxHeap.remove(num);
        }
        else {
            minHeap.remove(num);
        }
        if (maxHeap.size() > minHeap.size()) {
            minHeap.add(maxHeap.poll());
        }
        if (minHeap.size() - maxHeap.size() > 1) {
            maxHeap.add(minHeap.poll());
        }
    }
	
    private double getMedian() {
        if (maxHeap.isEmpty() && minHeap.isEmpty()) {
            return 0;
        }
        if (maxHeap.size() == minHeap.size()) {
            return ((double) maxHeap.peek() + (double) minHeap.peek()) / 2.0;
        }
        else {
            return (double)minHeap.peek();
        }
    }
}
'''


