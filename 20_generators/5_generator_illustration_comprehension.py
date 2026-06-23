# Consider a use case where we have a list of numbers
nums = [1, 2, 3, 4, 5, 6, 7, 8]


# This is now a generator, not list comprehension/complete squaredlist
squared_nums = (x * x for x in nums)


print(squared_nums)


for sq in squared_nums:
    print(f"Some ops on {sq}")
