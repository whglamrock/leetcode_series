
# the problem description is very ambiguous to understand. It's
# actually looking for the maximum number of fruits you can collect
# the constraint is: you can only collect 2 types of fruits.
# when the 3rd type appears, the counting should only include the
# consecutive ones (e.g., 1,0,1,4, when 4 appears, we should only count
# 1,4)

# sliding window

class Solution(object):
    def totalFruit(self, tree):

        window = {}
        ans = 0

        for i in xrange(len(tree)):
            fruitType = tree[i]
            if fruitType not in window:
                if len(window) == 2:
                    # calculate the max
                    ans = max(ans, sum(window.values()))
                    # delete the left key
                    prevKey = tree[i - 1]
                    j = i - 1
                    window[prevKey] = 0
                    while tree[j] == prevKey:
                        window[prevKey] += 1
                        j -= 1
                    del window[tree[j]]
                window[fruitType] = 1
            else:
                window[fruitType] += 1

        if window:
            ans = max(ans, sum(window.values()))

        return ans



Sol = Solution()
print Sol.totalFruit([3,3,3,1,2,1,1,2,3,3,4])

