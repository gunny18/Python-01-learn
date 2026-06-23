nums = [1, 2, 3, 4, 5]

for num in nums:
    print(num)


for idx, num in enumerate(nums):
    print(idx, num)


for idx, num in enumerate(nums, start=10):
    print(idx, num)
