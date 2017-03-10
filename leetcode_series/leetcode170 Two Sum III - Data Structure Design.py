class TwoSum(object):

    def __init__(self):
        """
        initialize your data structure here
        """
        self.dick = {}


    def add(self, number):
        """
        Add the number to an internal data structure.
        :rtype: nothing
        """
        if number in self.dick:
            self.dick[number] += 1
        else:
            self.dick[number] = 1


    def find(self, value):
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        :type value: int
        :rtype: bool
        """
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

