
class BrowserHistory:
    def __init__(self, homepage: str):
        self.history = [homepage]
        self.curr = 0
        self.lastIndex = 0

    def visit(self, url: str) -> None:
        self.curr += 1
        if self.curr == len(self.history):
            self.history.append(url)
        else:
            self.history[self.curr] = url
        # this way we clear the forward history
        # so that all back and fwd operations won't go beyond lastIndex
        self.lastIndex = self.curr

    def back(self, steps: int) -> str:
        stepsToBack = min(steps, self.curr)
        self.curr -= stepsToBack
        return self.history[self.curr]

    def forward(self, steps: int) -> str:
        self.curr = min(self.curr + steps, self.lastIndex)
        return self.history[self.curr]


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)
