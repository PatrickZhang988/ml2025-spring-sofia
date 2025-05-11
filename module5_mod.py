class NumberManager:
    def __init__(self):
        self.numbers = []

    def insert_number(self, num):
        self.numbers.append(num)

    def search_number(self, x):
        # 从1开始编号，所以 +1，找不到就返回 -1
        if x in self.numbers:
            return self.numbers.index(x) + 1
        else:
            return -1
