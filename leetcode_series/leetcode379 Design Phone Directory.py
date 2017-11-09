
class PhoneDirectory(object):

    def __init__(self, maxNumbers):

        self.numpool = set()
        for i in xrange(maxNumbers):
            self.numpool.add(i)

    def get(self):

        strip = None
        for num in self.numpool:
            strip = num
            break
        if strip != None:
            self.numpool.discard(strip)
            return strip
        return -1

    def check(self, number):

        return number in self.numpool

    def release(self, number):

        self.numpool.add(number)



# Your PhoneDirectory object will be instantiated and called as such:
# obj = PhoneDirectory(maxNumbers)
# param_1 = obj.get()
# param_2 = obj.check(number)
# obj.release(number)