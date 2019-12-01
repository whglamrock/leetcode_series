
from collections import defaultdict

# DFS approach, more efficient

class Solution(object):
    def accountsMerge(self, accounts):

        visited = set()
        # build the map
        email_to_accounts = defaultdict(list)
        for i, account in enumerate(accounts):
            for email in account[1:]:
                email_to_accounts[email].append(i)

        # cannot delete from the email_to_accounts[email], otherwise there will be for loop error
        #   emails is a set that stores the emails related to this name
        def dfs(name_idx, emails):
            if name_idx in visited:
                return
            visited.add(name_idx)
            for email in accounts[name_idx][1:]:
                emails.add(email)   # the variable emails has to be a set
                for neighbor in email_to_accounts[email]:
                    dfs(neighbor, emails)
            return emails

        ans = []
        # do the dfs and collect the answer
        for i, account in enumerate(accounts):
            name = account[0]
            emails = dfs(i, set())
            if emails:
                ans.append([name] + sorted(emails))

        return ans