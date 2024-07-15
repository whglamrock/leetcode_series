class Logger:
    def __init__(self):
        self.messageToLastTime = {}

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if message not in self.messageToLastTime:
            self.messageToLastTime[message] = timestamp
            return True

        lastTime = self.messageToLastTime[message]
        if timestamp < lastTime + 10:
            return False
        self.messageToLastTime[message] = timestamp
        return True


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)
