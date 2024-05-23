from threading import Semaphore, Barrier

class H2O:
    def __init__(self):
        self.semH = Semaphore(2)
        self.semO = Semaphore(1)
        self.bar = Barrier(3)

    def hydrogen(self, releaseHydrogen: 'Callable[[], None]') -> None:
        with self.semH:
            self.bar.wait()
            # releaseHydrogen() outputs "H". Do not change or remove this line.
            releaseHydrogen()

    def oxygen(self, releaseOxygen: 'Callable[[], None]') -> None:
        with self.semO:
            self.bar.wait()
            # releaseOxygen() outputs "O". Do not change or remove this line.
            releaseOxygen()
