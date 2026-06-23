import random

val = random.random()
print(val)

val = random.uniform(1, 10)
print(val)

val = random.randint(1, 6)
print(val)

names = ["Alex", "Hall", "Ashton", "Yuki"]
val = random.choice(names)
print(val)


colors = ["Red", "Black", "Green"]
# choices selects elements with replacement i.e. elements can appear again (Sampling with replacement)
val = random.choices(colors, k=10)
print(val)

# It means final list will have 45% red, 45% black and 10% green
# More weight = More chances of that element getting selected
val = random.choices(colors, k=10, weights=[45, 45, 10])
print(val)


deck = list(range(1, 53))
print(deck)
random.shuffle(deck)
print(deck)

# sample selcets elements without replacement, i.e. same element cannot appear again (Sampling without replacement)
hand = random.sample(deck, k=5)
print(hand)
