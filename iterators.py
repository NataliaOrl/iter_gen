nested_list = [
	['a', 'b', 'c'],
	['d', 'e', 'f', 'h', False],
	[1, 2, None],
]

class FlatIterator:
    def __init__(self, wrapped):
        self.wrapped = wrapped
        self.cursor2 = 0
        self.cursor1 = 0

    def __iter__(self):
        return self
  
    def __next__(self):
        while self.cursor2 == len(self.wrapped[self.cursor1]):
            self.cursor2 = 0
            self.shift()
            continue             
        else:
            item = self.wrapped[self.cursor1][self.cursor2]
            self.cursor2 += 1
            return item

    def shift(self):
        if self.cursor1 == len(self.wrapped) - 1:
            raise StopIteration
        else:
            self.cursor1 += 1


if __name__ == '__main__':
    for item in FlatIterator(nested_list):
        print(repr(item))

    flat_list = [item for item in FlatIterator(nested_list)]
    print(flat_list)
