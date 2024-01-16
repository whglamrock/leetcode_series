from typing import List

# O(N * 120), essentially O(N) time
class Solution(object):
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        timeToNameToCities = {}
        invalidTxns = []
        for txn in transactions:
            items = txn.split(",")
            name = items[0]
            time = int(items[1])
            city = items[3]

            if time not in timeToNameToCities:
                timeToNameToCities[time] = {name: [city]}
            else:
                if name not in timeToNameToCities[time]:
                    timeToNameToCities[time][name] = [city]
                else:
                    timeToNameToCities[time][name].append(city)

        for txn in transactions:
            items = txn.split(",")
            name = items[0]
            time = int(items[1])
            money = int(items[2])
            city = items[3]

            if money > 1000:
                invalidTxns.append(txn)
                continue

            for i in range(time - 60, time + 61):
                if i not in timeToNameToCities:
                    continue
                if name not in timeToNameToCities[i]:
                    continue
                if len(timeToNameToCities[i][name]) > 1 or (timeToNameToCities[i][name][0] != city):
                    invalidTxns.append(txn)
                    break

        return invalidTxns
