class FreqStack:

    def __init__(self):
        self.cnt = defaultdict(list)
        self.max_count = 0
        self.stacks = {}

    def push(self, val: int) -> None:
        val_count = self.cnt.get(val, 0) + 1
        self.cnt[val] = val_count
        if val_count > self.max_count:
            self.max_count = val_count
            self.stacks[val_count] = []
        self.stacks[val_count].append(val)

    def pop(self) -> int:
        res = self.stacks[self.max_count].pop()
        self.cnt[res] -= 1
        if not self.stacks[self.max_count]:
            self.max_count -= 1
        return res
 
# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()