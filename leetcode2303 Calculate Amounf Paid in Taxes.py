from typing import List

class Solution:
    def calculateTax(self, brackets: List[List[int]], income: int) -> float:
        tax = 0
        for i in range(len(brackets)):
            lower = brackets[i - 1][0] if i > 0 else 0
            upper, percent = brackets[i]
            if income <= lower:
                break
            tax += (min(upper, income) - lower) * percent / 100

        return tax
