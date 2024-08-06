from threading import Thread
from time import time, sleep
from typing import Callable


# without threadpool. If we are asked about using a threadPool, we will need future and ThreadPoolExecutor library,
# which loses the whole point of this exercise.
class DelayedScheduler:
    def __init__(self):
        self.functions = []
        t = Thread(target=self.poll)
        t.start()

    def poll(self):
        while True:
            # now is in milliseconds
            now = time() * 1000

            # assuming the dueTime is millisecond epoch timestamp
            for function, dueTime in self.functions:
                if now >= dueTime:
                    function()

            self.functions = []
            for function, dueTime in self.functions:
                if dueTime > now:
                    self.functions.append((function, dueTime))

            # 1/4 second, can be configurable
            sleep(0.25)

    def scheduleWithInitialDelay(self, function: Callable, initialDelay: int):
        self.functions.append((function, initialDelay))

    def scheduleWithInitialDelayAndInterval(self, function: Callable, initialDelay: int, interval: int):
        pass

