from collections import deque
from concurrent import futures
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
        hostname = lambda url: url.split('/')[2]
        visited = {startUrl}

        with futures.ThreadPoolExecutor(max_workers=32) as executor:
            tasks = deque([executor.submit(htmlParser.getUrls, startUrl)])
            while tasks:
                for url in tasks.popleft().result():
                    if url not in visited and hostname(startUrl) == hostname(url):
                        visited.add(url)
                        tasks.append(executor.submit(htmlParser.getUrls, url))

        return list(visited)
