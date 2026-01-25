# list
nums = [1, 2, 3, 4, 5, 6, 7]

my_list = []
for n in nums:
    my_list.append(n)
print(my_list)

my_list = [n for n in nums]
print(my_list)

# comprehensions are more readable than map
my_list = map(lambda n: n * n, nums)
print(my_list)
my_list = [n * n for n in nums]
print(my_list)

# comprehensions are more readable than filter!
my_list = filter(lambda n: n % 2 == 0, nums)
print(my_list)
my_list = [n for n in nums if n % 2 == 0]
print(my_list)


my_list = [(n, i) for n in nums for i in range(4)]
print(my_list)

# Dicts
names = ["Arun", "Sasdasd", "qweqweqwe", "qqqqes"]
ranks = [1, 2, 3, 4]
print(zip(names, ranks))

my_dict = {}
for name, rank in zip(names, ranks):
    my_dict[name] = rank
print(my_dict)

my_dict = {name: rank for name, rank in zip(names, ranks)}
print(my_dict)


# sets
my_set = {n for n in nums}
print(my_set)
