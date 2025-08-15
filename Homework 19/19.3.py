class MyIterable:
    def __init__(self, data):
        self.data = data

    def __iter__(self):
        return iter(self.data)

    def __getitem__(self, index):
        return self.data[index]
