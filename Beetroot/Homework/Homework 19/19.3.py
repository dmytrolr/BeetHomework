class MyIterable:
    def __init__(self, data):
        self.data = data

    def __iter__(self):
        return iter(self.data)

    def __getitem__(self, index):
        return self.data[index]

# obj = MyIterable(['a', 'b', 'c'])
#
# for item in obj:
#     print(item)
#
# print(obj[0])
# print(obj[2])
