
# in every combination of sum3, make sure that three numbers are in ascending order

class Solution(object):
    def combinationSum3(self, k, n):

        if k == 1:
            return [[n]]
        if n < k*(k+1)/2:   # e.g. k=3, n=5: can't find 3 unique numbers add up to 5
            return []
        ans = []
        while k>0:
            if (not ans):
                for i in xrange(1,n/k+1):
                    if n-i <= 9*(k-1)-(k-1)*(k-2)/2:  # ensures that the first number is no more than 9
                        ans.append([i,n-i])  # deduct the 'n' by the newly added value
                if (not ans):
                    return []
            else:
                new = []
                if k != 1:
                    for item in ans:
                        remain = item.pop()
                        for i in xrange(item[-1]+1,remain/k+1):
                            if (remain-i) <= 9*(k-1)-(k-1)*(k-2)/2:  # ensures that the first number is no more than 9
                                new.append(item+[i,remain-i])  # the last element stores the remaining value of 'n'
                else:
                    for item in ans:
                        last = item.pop()
                        if last != item[-1]:  # the 'del' operator can't delete list from list[list]
                            new.append(item+[last])  # thus create a new list[list]
                ans = new
            k -= 1

        return ans