from threading import Lock

class Foo:
    def __init__(self):
        self.firstLock, self.secondLock, self.thirdLock = Lock(), Lock(), Lock()
        self.secondLock.acquire()
        self.thirdLock.acquire()

    def first(self, printFirst: 'Callable[[], None]') -> None:
        self.firstLock.acquire()
        # printFirst() outputs "first". Do not change or remove this line.
        printFirst()
        self.secondLock.release()

    def second(self, printSecond: 'Callable[[], None]') -> None:
        self.secondLock.acquire()
        # printSecond() outputs "second". Do not change or remove this line.
        printSecond()
        self.thirdLock.release()

    def third(self, printThird: 'Callable[[], None]') -> None:
        self.thirdLock.acquire()
        # printThird() outputs "third". Do not change or remove this line.
        printThird()
        self.firstLock.release()
