
class StockSpanner:
    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        ans = 1
        # between 2 consecutive elements, there are some popped out smaller elements which are counted
        # by stack[i][1]. We won't double count any popped out smaller elements because
        # each stack[i][1] only counts the number of consecutive smaller elements on stack[i][0]'s left until
        # stack[i - 1][0] and stack[i - 1][0] > stack[i][0]
        while self.stack and self.stack[-1][0] <= price:
            ans += self.stack.pop()[1]
        self.stack.append([price, ans])
        return ans


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)


'''
# original solution which saves the index of each decreasing stack element, 
# then using binary search to count the number smaller elements.
class StockSpanner:
    def __init__(self):
        self.decreasingStack = []
        self.size = 0

    def next(self, price: int) -> int:
        while self.decreasingStack and self.decreasingStack[-1][1] < price:
            self.decreasingStack.pop()
        self.decreasingStack.append([self.size, price])
        self.size += 1

        return self.findNumOfSmallerOrEqualElements(price, self.size - 1)

    def findNumOfSmallerOrEqualElements(self, target: int, currIndex: int) -> int:
        l, r = 0, len(self.decreasingStack) - 1
        while l <= r:
            m = (l + r + 1) // 2
            if l == r:
                if self.decreasingStack[m][1] > target:
                    return currIndex - self.decreasingStack[m][0]
                else:
                    return self.size
            if self.decreasingStack[m][1] <= target:
                r = m - 1
            else:
                l = m

        return 0
'''