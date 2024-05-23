from threading import Lock

class ZeroEvenOdd:
    def __init__(self, n):
        self.n = n
        self.zeroLock = Lock()
        self.evenLock = Lock()
        self.oddLock = Lock()
        self.evenLock.acquire()
        self.oddLock.acquire()

    # printNumber(x) outputs "x", where x is an integer.
    def zero(self, printNumber: 'Callable[[int], None]') -> None:
        for i in range(1, self.n + 1):
            self.zeroLock.acquire()
            printNumber(0)

            if i % 2:
                self.oddLock.release()
            else:
                self.evenLock.release()

    def even(self, printNumber: 'Callable[[int], None]') -> None:
        for i in range(2, self.n + 1, 2):
            self.evenLock.acquire()
            printNumber(i)
            self.zeroLock.release()

    def odd(self, printNumber: 'Callable[[int], None]') -> None:
        for i in range(1, self.n + 1, 2):
            self.oddLock.acquire()
            printNumber(i)
            self.zeroLock.release()
