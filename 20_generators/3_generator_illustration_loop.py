nums = [1, 2, 3, 4, 5, 6, 7, 8]


def squared_nums_generator(nums):
    for num in nums:
        yield num * num


sq_nums = squared_nums_generator(nums)

# This is now a generator object
print(sq_nums)

# We can also use a loop to retrieve generated values one at a time, which was exactly the purposeof generators
for sq in sq_nums:
    print(f"Some ops with {sq}")
