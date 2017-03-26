
class TwoSum(object):

    def __init__(self):

        self.dick = {}

    def add(self, number):

        if number in self.dick:
            self.dick[number] += 1
        else:
            self.dick[number] = 1

    def find(self, value):

        for item in self.dick:
            if value-item in self.dick:
                if value-item != item or self.dick[item]>1:
                    return True

        return False



Sol = TwoSum()
Sol.add(0)
Sol.add(-1)
Sol.add(1)
print Sol.find(0)

