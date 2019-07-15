
from collections import defaultdict, deque

class Solution(object):
    def subdomainVisits(self, cpdomains):
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """
        domainCount = defaultdict(int)
        for cpdomain in cpdomains:
            splitted = cpdomain.split(' ')
            count, domain = int(splitted[0]), splitted[1]

            subdomains = domain.split('.')
            currDomain = deque()
            for subdomain in subdomains[::-1]:
                currDomain.appendleft(subdomain)
                domainCount['.'.join(currDomain)] += count

        ans = []
        for domain in domainCount:
            ans.append(str(domainCount[domain]) + ' ' + domain)

        return ans



print Solution().subdomainVisits(cpdomains = ["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"])
