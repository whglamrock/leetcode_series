
class ProductOfNumbers:
    def __init__(self):
        self.last0Distance = 0
        # the key is the distance to last 0, value is the prefix product after the last 0
        # if the stream is [3, 0, 2, 4, 5], then non0IndexToPrefixProduct is {1: 2, 2: 8, 3: 40}
        self.non0IndexToPrefixProduct = {}
        self.product = 0

    def add(self, num: int) -> None:
        if num == 0:
            self.last0Distance = 0
            self.non0IndexToPrefixProduct = {}
            self.product = 0
        else:
            self.last0Distance += 1
            if self.product == 0:
                self.product = num
            else:
                self.product *= num
            self.non0IndexToPrefixProduct[self.last0Distance] = self.product

    def getProduct(self, k: int) -> int:
        if k > self.last0Distance:
            return 0

        if k == self.last0Distance:
            return self.product

        return self.product // self.non0IndexToPrefixProduct[self.last0Distance - k]


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)
