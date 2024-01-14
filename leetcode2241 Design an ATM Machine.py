from collections import defaultdict
from typing import List

class ATM:
    def __init__(self):
        self.bankNoteToCount = defaultdict(int)

    def deposit(self, banknotesCount: List[int]) -> None:
        self.bankNoteToCount[20] += banknotesCount[0]
        self.bankNoteToCount[50] += banknotesCount[1]
        self.bankNoteToCount[100] += banknotesCount[2]
        self.bankNoteToCount[200] += banknotesCount[3]
        self.bankNoteToCount[500] += banknotesCount[4]

    def withdraw(self, amount: int) -> List[int]:
        numOf500, numOf200, numOf100, numOf50, numOf20 = 0, 0, 0, 0, 0
        if amount >= 500:
            numOf500 = min(amount // 500, self.bankNoteToCount[500])
            amount -= numOf500 * 500
        if amount >= 200:
            numOf200 = min(amount // 200, self.bankNoteToCount[200])
            amount -= numOf200 * 200
        if amount >= 100:
            numOf100 = min(amount // 100, self.bankNoteToCount[100])
            amount -= numOf100 * 100
        if amount >= 50:
            numOf50 = min(amount // 50, self.bankNoteToCount[50])
            amount -= numOf50 * 50
        if amount >= 20:
            numOf20 = min(amount // 20, self.bankNoteToCount[20])
            amount -= numOf20 * 20

        if amount > 0:
            return [-1]

        self.bankNoteToCount[500] -= numOf500
        self.bankNoteToCount[200] -= numOf200
        self.bankNoteToCount[100] -= numOf100
        self.bankNoteToCount[50] -= numOf50
        self.bankNoteToCount[20] -= numOf20
        return [numOf20, numOf50, numOf100, numOf200, numOf500]


# Your ATM object will be instantiated and called as such:
# obj = ATM()
# obj.deposit(banknotesCount)
# param_2 = obj.withdraw(amount)
