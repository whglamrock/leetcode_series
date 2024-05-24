from collections import deque
from typing import List

# """
# This is HtmlParser's API interface.
# You should not implement it, or speculate about its implementation
# """
class HtmlParser(object):
    def getUrls(self, url):
        """
       :type url: str
       :rtype List[str]
       """

class Solution:
    def crawl(self, startUrl: str, htmlParser: 'HtmlParser') -> List[str]:
        def getHostName(url):
            start = len('http://')
            i = start
            while i < len(url):
                if url[i] == '/':
                    break
                i += 1
            return url[start:i]

        q = deque([startUrl])
        seen = {startUrl}
        while q:
            url = q.popleft()
            for nextUrl in htmlParser.getUrls(url):
                if nextUrl not in seen and getHostName(nextUrl) == getHostName(startUrl):
                    seen.add(nextUrl)
                    q.append(nextUrl)

        return list(seen)
