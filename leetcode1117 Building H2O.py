from threading import Semaphore, Barrier

class H2O:
    def __init__(self):
        self.semH, self.semO = Semaphore(2), Semaphore(1)
        self.bar = Barrier(3)

    def hydrogen(self, releaseHydrogen: 'Callable[[], None]') -> None:
        with self.semH:
            # releaseHydrogen() outputs "H". Do not change or remove this line.
            releaseHydrogen()
            self.bar.wait()

    def oxygen(self, releaseOxygen: 'Callable[[], None]') -> None:
        with self.semO:
            # releaseOxygen() outputs "O". Do not change or remove this line.
            releaseOxygen()
            self.bar.wait()
