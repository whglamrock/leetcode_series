
# super easy OOD question.

class Logger(object):

    def __init__(self):

        self.dick = {}

    def shouldPrintMessage(self, timestamp, message):

        if message not in self.dick:
            self.dick[message] = timestamp
            return True
        else:
            if timestamp - self.dick[message] >= 10:
                self.dick[message] = timestamp
                return True
            else:
                return False



# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)