class MinStack:
    def __init__(self):
        self.stack = []

    def push(self, num):
        if not self.stack:
            min_num = num
        else:
            min_num = min(self.stack[-1][1], num)
        self.stack.append((num, min_num))

    def pop(self):
        if not self.stack:
            return None
        val, _ = self.stack.pop()
        return val

    def top(self):
        return self.stack[-1][0] if self.stack else None

    def getMin(self):
        return self.stack[-1][1] if self.stack else None