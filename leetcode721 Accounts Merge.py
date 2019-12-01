
from collections import defaultdict

# DFS approach, more straightforward / easier then Union-Find

class Solution(object):
    def accountsMerge(self, accounts):
        """
        :type accounts: List[List[str]]
        :rtype: List[List[str]]
        """

        emailToAccounts = defaultdict(list)
        for i, account in enumerate(accounts):
            for email in account[1:]:
                emailToAccounts[email].append(i)

        ans = []
        visited = set()
        for i in xrange(len(accounts)):
            emails = set()
            self.dfs(i, accounts, emailToAccounts, emails, visited)
            if emails:
                ans.append([accounts[i][0]] + sorted(emails))

        return ans

    def dfs(self, account_index, accounts, emailToAccounts, emails, visited):
        if account_index in visited:
            return
        visited.add(account_index)
        for email in accounts[account_index][1:]:
            emails.add(email)
            for neighbor in emailToAccounts[email]:
                self.dfs(neighbor, accounts, emailToAccounts, emails, visited)
