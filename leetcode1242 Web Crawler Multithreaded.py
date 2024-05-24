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
        def getHostName(url):
            start = len('http://')
            i = start
            while i < len(url):
                if url[i] == '/':
                    break
                i += 1
            return url[start:i]

        seen = {startUrl}
        with futures.ThreadPoolExecutor(max_workers=16) as executor:
            q = deque([executor.submit(htmlParser.getUrls, startUrl)])
            while q:
                for url in q.popleft().result():
                    if url not in seen and getHostName(url) == getHostName(startUrl):
                        q.append(executor.submit(htmlParser.getUrls, url))
                        seen.add(url)

        return list(seen)


'''
from threading import Lock, Thread
from queue import Queue

# solution using lock
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
        
        seen = {startUrl}
        q = Queue()
        lock = Lock()

        def work():
            while True:
                url = q.get()
                if url is None:
                    return
                
                for nextUrl in htmlParser.getUrls(url):
                    with lock:
                        if nextUrl not in seen and getHostName(nextUrl) == getHostName(startUrl):
                            seen.add(nextUrl)
                            q.put(nextUrl)
                
                q.task_done()
        
        workers = []
        for i in range(16):
            t = Thread(target=work)
            t.start()
            workers.append(t)

        # make sure all tasks are finished before we proceed
        q.put(startUrl)
        q.join()

        # to exit each thread
        for i in range(16):
            q.put(None)
        for t in workers:
            t.join()

        return list(seen)
'''