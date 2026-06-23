nums = [1, 2, 3, 4, 5, 6, 7, 8]


def squared_nums_generator(nums):
    for num in nums:
        yield num * num


sq_nums = squared_nums_generator(nums)

# This is now a generator object
print(sq_nums)

# next(generator_obj) -> gives the value after computation. Here gives square of first element
# If end of list reached, raises StopIteration Error
print(next(sq_nums))
print(next(sq_nums))
print(next(sq_nums))
print(next(sq_nums))
print(next(sq_nums))
print(next(sq_nums))
print(next(sq_nums))
print(next(sq_nums))
# At this point generator is done, cannot generate more values. Hence raises StopIteration if next is called at this stage
next(sq_nums)
