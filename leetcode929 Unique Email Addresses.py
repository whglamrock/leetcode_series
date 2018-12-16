
# it's guaranteed that each email will only contain one '@'

class Solution(object):
    def numUniqueEmails(self, emails):

        uniqueSet = set()
        for email in emails:
            delimiterIndex = email.index('@')
            local = []
            for char in email[:delimiterIndex]:
                if char == '.':
                    continue
                elif char == '+':
                    break
                local.append(char)
            uniqueEmail = ''.join(local) + email[delimiterIndex + 1:]
            uniqueSet.add(uniqueEmail)

        return len(uniqueSet)



Sol = Solution()
emails = ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]
print Sol.numUniqueEmails(emails)


