
from collections import defaultdict

# advanced union find approach

class Solution(object):
    def accountsMerge(self, accounts):

        # key is the account email, value is the name.
        #   it is guaranteed that same person will always have the same name
        email_to_nameIndex = defaultdict(int)
        nameIndex_to_emails = defaultdict(set)
        for i, account in enumerate(accounts):
            # collect all related nameIndices that will need to be united
            related_name_indices = []
            for j in xrange(1, len(account)):
                email = account[j]
                if email in email_to_nameIndex:
                    nameIndex = email_to_nameIndex[email]
                    related_name_indices.append(nameIndex)
            # add the new accounts to maps
            for j in xrange(1, len(account)):
                email = account[j]
                email_to_nameIndex[email] = i
                nameIndex_to_emails[i].add(email)
            # union
            for related_nameIndex in related_name_indices:
                related_emails = nameIndex_to_emails[related_nameIndex]
                # point the email to the new nameIndex
                for related_email in related_emails:
                    email_to_nameIndex[related_email] = i
                # set union
                nameIndex_to_emails[i] |= related_emails
                # delete old index entry
                del nameIndex_to_emails[related_nameIndex]

        ans = []
        for nameIndex in nameIndex_to_emails:
            emailSet = nameIndex_to_emails[nameIndex]
            name = accounts[nameIndex][0]
            ans.append([name] + sorted(emailSet))

        return ans

