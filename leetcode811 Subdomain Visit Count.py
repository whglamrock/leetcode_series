from collections import defaultdict
from typing import List


class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        domainCount = defaultdict(int)
        for cpDomain in cpdomains:
            count, domain = cpDomain.split(' ')
            count = int(count)
            tokens = domain.split('.')
            for i in range(len(tokens)):
                subDomain = '.'.join(tokens[i:])
                domainCount[subDomain] += count

        ans = []
        for domain, count in domainCount.items():
            ans.append(str(count) + ' ' + domain)
        return ans
