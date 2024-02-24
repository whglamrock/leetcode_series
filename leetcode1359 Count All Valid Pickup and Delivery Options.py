
# Should be a medium level question.
# 1) After completing n - 1 orders, for nth order, we have 2n - 1 positions to insert Pn, Dn.
# 2) For example, when n == 3, and one of n - 1 order option is P1,P2,D1,D2, the positions to insert P3, D3 are:
# (position) P1 (position) P2 (position) D1 (position) D2 (position), and you just need to make sure D3 is inserted
# after P3. e.g., if P3 is inserted after P2 (3rd position), D3 can only be inserted in 3rd, 4th, and 5th positions
# so the total num of options is 5 + 4 + 3 + 2 + 1.
# 3) From 2) we can come up with formula: for nth order we have 2n - 1 + 2n - 2 + .. + 1 = n * (2n - 1).
# 4) Consider the num of options is f(n), so the overall answer is f(n) * f(n - 1) * .. f(1)
class Solution:
    def countOrders(self, n: int) -> int:
        ans = 1
        for i in range(1, n + 1):
            ans *= i * (2 * i - 1)

        return ans % (10 ** 9 + 7)
