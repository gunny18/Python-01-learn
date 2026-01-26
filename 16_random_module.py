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
val = random.choices(colors, k=10)
print(val)


val = random.choices(colors, k=10, weights=[45, 45, 10])
print(val)


deck = list(range(1, 53))
print(deck)
random.shuffle(deck)
print(deck)

hand = random.sample(deck, k=5)
print(hand)
