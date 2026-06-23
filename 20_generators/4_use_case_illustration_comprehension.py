# Consider a use case where we have a list of numbers
nums = [1, 2, 3, 4, 5, 6, 7, 8]


# Consider we need a list of the above numbers, squared
# Say we dosomething like below
# Get the squared list
squared_nums = [x * x for x in nums]

# Now say we need to perform some actions on each of the items in squared list
# But at no point in time I need access to the entire squared list. I just need to perform some action one element at a time
for sq in squared_nums:
    print(f"Some ops on {sq}")

# Imagine if above was done for 1 Million elements.
# And we have squares of all 1 million elements in memory, though we don't need all at same time
# Exactly where generator shines and helps improve performance and space utilization
