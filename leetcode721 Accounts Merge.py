
from collections import defaultdict

# DFS approach, more efficient

class Solution(object):
    def accountsMerge(self, accounts):

        visited = [False] * len(accounts)
        # build the map
        email_to_accounts = defaultdict(list)
        for i, account in enumerate(accounts):
            for email in account[1:]:
                email_to_accounts[email].append(i)

        # cannot delete from the email_to_accounts[email], otherwise there will be for loop error
        #   emails is a set that stores the emails related to this name
        def dfs(name_idx, emails):
            if visited[name_idx]:
                return
            visited[name_idx] = True
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



'''
from collections import defaultdict

# classic union find, more efficient than the "find related name index that needs to be united" approach

class Solution(object):
    def accountsMerge(self, accounts):
        # key is the child, value is the parent
        parents = {}
        # email to name mapping
        owner = {}

        # initial setup
        for acc in accounts:
            for i in xrange(1, len(acc)):
                parents[acc[i]] = acc[i]
                owner[acc[i]] = acc[0]

        # within each account, the ROOT parent of each email is same -- the root parent of first email
        for acc in accounts:
            rootP = self.find(acc[1], parents)
            for i in xrange(2, len(acc)):
                rootP_i = self.find(acc[i], parents)
                parents[rootP_i] = rootP

        # union (after this point, the parents graph won't change)
        union = defaultdict(set)	# mapping from the root parent to all its children
        for acc in accounts:
            # first email is the parent of other emails in this account, and it's guaranteed that we can
            # 	find the ultimate root parent from this first email
            rootP = self.find(acc[1], parents)
            for i in xrange(1, len(acc)):
                union[rootP].add(acc[i])

        ans = []
        for rootP in union:
            name = owner[rootP]
            emails = sorted(union[rootP])
            ans.append([name] + emails)

        return ans
    
    # remember this method
    def find(self, child, parents):
        return child if parents[child] == child else self.find(parents[child], parents)
'''

