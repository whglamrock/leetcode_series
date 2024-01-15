from typing import List

class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        ans = [str(i) for i in range(n + 1)]
        for i in range(1, n + 1):
            if i % 3 == 0 and i % 5 == 0:
                ans[i] = 'FizzBuzz'
            elif i % 3 == 0:
                ans[i] = 'Fizz'
            elif i % 5 == 0:
                ans[i] = 'Buzz'
        ans.pop(0)
        return ans
