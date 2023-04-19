# input
original_list = [(4, 5), (4, ), (8, 6, 7), (1, ), (3, 4, 6, 7)]
k = 1

# use map() and a lambda function to filter out tuples of length k
filtered_list = list(map(lambda x: x, filter(lambda x: len(x) != k, original_list)))

# output
print(filtered_list)
