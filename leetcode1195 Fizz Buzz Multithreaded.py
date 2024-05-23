from threading import Lock

class FizzBuzz:
    def __init__(self, n: int):
        self.n = n
        self.fizzLock, self.buzzLock, self.fizzBuzzLock, self.mainLock = Lock(), Lock(), Lock(), Lock()
        self.fizzLock.acquire()
        self.buzzLock.acquire()
        self.fizzBuzzLock.acquire()
        self.done = False

    # printFizz() outputs "fizz"
    def fizz(self, printFizz: 'Callable[[], None]') -> None:
        while True:
            self.fizzLock.acquire()
            if self.done:
                return
            printFizz()
            self.mainLock.release()

    # printBuzz() outputs "buzz"
    def buzz(self, printBuzz: 'Callable[[], None]') -> None:
        while True:
            self.buzzLock.acquire()
            if self.done:
                return
            printBuzz()
            self.mainLock.release()

    # printFizzBuzz() outputs "fizzbuzz"
    def fizzbuzz(self, printFizzBuzz: 'Callable[[], None]') -> None:
        while True:
            self.fizzBuzzLock.acquire()
            if self.done:
                return
            printFizzBuzz()
            self.mainLock.release()

    # printNumber(x) outputs "x", where x is an integer.
    def number(self, printNumber: 'Callable[[int], None]') -> None:
        for i in range(1, self.n + 1):
            self.mainLock.acquire()
            if i % 15 == 0:
                self.fizzBuzzLock.release()
            elif i % 3 == 0:
                self.fizzLock.release()
            elif i % 5 == 0:
                self.buzzLock.release()
            else:
                printNumber(i)
                self.mainLock.release()

        # we need to acquire lock here to block the following lines until getting the lock; also
        # in other methods calling self.mainLock.release() when mainLock is not acquired will throw error
        self.mainLock.acquire()
        self.done = True
        # 1) self.mainLock.acquire() -> putting it here instead of line 53 will cause TLE in LC.
        # because the self.done is a global variable shared across threads so it's better to require a lock
        # before modifying its value
        # 2) we need to release lock for the while loops in other methods to loop to the next one to hit the exit
        # condition (self.done == True)
        self.fizzLock.release()
        self.buzzLock.release()
        self.fizzBuzzLock.release()
