message = "Hello"

message_1 = "Hello'qqq"

message_2 = 'Hello"we'

message_3 = """Hello, My name is
Gunny."""

message_4 = '''
Hi
I
am
Death!
'''

print(message)
print(message_1[3])

# Index Error
# print(message_1[199])

# Length of str
print(len(message_1))

# str concat
message_5 = message_1 + message_2

# string format
message_6 = "{}, {}".format(message, message_1)

# f-string
message_7 = f"{message} asdasd {message_1}."

# Slicing
print(message_1[1:3])
print(message_1[:5])
print(message_1[3:6])
print(message_1[3:])
print(message[:])

# Methods
print(message.lower())
print(message.upper())
print(message.count("e"))
print(message.find("lo"))
replaced_message = message.replace("Hel", "WTFFFF")

