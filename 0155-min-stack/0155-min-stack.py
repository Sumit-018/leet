class MinStack:

    def __init__(self):
        self.st = []
        self.minstack = []

    def push(self, val: int) -> None:
        self.st.append(val)
        if not self.minstack or self.minstack[-1] >= val:
            self.minstack.append(val)

    def pop(self) -> None:
        x = self.st.pop()
        if x == self.minstack[-1]:
            self.minstack.pop()

    def top(self) -> int:
        return self.st[-1]

    def getMin(self) -> int:
        return self.minstack[-1]
