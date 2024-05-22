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
from queue import Queue
import threading

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
        
        queue = Queue()
        lock = threading.Lock()
        seen = {startUrl}

        def workThread():
            while True:
                url = queue.get()
                if url is None:
                    return
                
                for nextUrl in htmlParser.getUrls(url):
                    lock.acquire()
                    if nextUrl not in seen and getHostName(nextUrl) == getHostName(startUrl):
                        seen.add(nextUrl)
                        queue.put(nextUrl)
                    lock.release()
                
                queue.task_done()

        numOfWorkers = 16
        workers = []
        for i in range(numOfWorkers):
            t = threading.Thread(target=workThread)
            t.start()
            workers.append(t)
        
        queue.put(startUrl)
        queue.join()

        for i in range(numOfWorkers):
            queue.put(None)
        for t in workers:
            t.join()
        
        return list(seen)
'''