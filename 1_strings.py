# Double quotes to write string
message = "Hello"

# In case single quote is part of string
message_1 = "Hello'qqq"

# Use of single quote string and if " is part of string
message_2 = 'Hello"we'

# Multiline string using double quote
message_3 = """Hello, My name is
Gunny."""


# Multiline string using single quote
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

# Slicing - inclusive of start index, exclusive of end index
print(message_1[1:3])
print(message_1[:5])
print(message_1[3:6])
print(message_1[3:])
print(message[:])

# Methods on string data.

# Returns new string, does not modify orginal string
print(message.lower())
print(message.upper())
replaced_message = message.replace("Hel", "WTFFFF")

# Returns occureces of string/sequence
print(message.count("e"))

# Returns index of first sub-string if found.
print(message.find("lo"))
