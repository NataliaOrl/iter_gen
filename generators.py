nested_list = [
	['a', 'b', 'c'],
	['d', 'e', 'f'],
	[1, 2, None],
]

def flat_generator(nested_list):
    for el in nested_list:
        for item in el:
            yield item

if __name__ == '__main__':
    for item in  flat_generator(nested_list):
        print(item)
    flat_list = (item for item in flat_generator(nested_list))
    print(list(flat_list))