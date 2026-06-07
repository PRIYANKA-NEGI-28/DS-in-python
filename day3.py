# take input to make a list from user 
size=int(input("Enter the size"))
lis1=[]
lis2=[]
i=1
while i<=size:
  a=int(input())
  lis1.append(a)
  i=i+1
print(lis1)
i=1
while i<=size:
  b=int(input())
  lis2.append(b)
  i=i+1
print(lis2)


# add elements of list1 and 2  and make a list 3 = list1+ list2
lis1 = [1, 2, 3]

lis2 = [4, 5, 6]

lis3 = []

i = 0

while i < 3:

    s = lis1[i] + lis2[i]

    lis3.append(s)

    i = i + 1

print(lis3)




# Functions in Python
def multiplication(a, b):
    return a * b

print(multiplication(10, 5))

result = multiplication(10, 3)
print(result)


# def → used to create a function.
# a, b → parameters.
# return → sends the answer back.
# multiplication(10,5) → function call.


# Lambda Functions (One-Line Functions)
add_two_numbers = lambda a, b: a + b

print(add_two_numbers(20, 5))





# Removing Spaces

# strip() → Removes spaces from both sides
s = "    Hello    "
print(s.strip())


# lstrip() → Removes spaces from left side
print(s.lstrip())


# rstrip() → Removes spaces from right side
print(s.rstrip())



# spliting text
s = "Hello My Name Is priyanka"

print(s.split())

# Joining Text
letters = ["P", "Y", "T", "H", "O", "N"]

print("".join(letters))


# Replacing Text
s = "Hello My Name Is priyanka"
print(s.replace("Hello", "Hi"))





# Changing Letter Case
s = "HeLLo mY namE IS priyanka"

# lower()
print(s.lower())

# upper()
print(s.upper())


# title()
print(s.title())


# capitalize()
print(s.capitalize())






# Finding Text
s = "HeLLo mY namE IS Kavya"
find()
print(s.find("mY"))


# Returns index if found.
# Returns -1 if not found.



# Checking Start and End

s = "Hello World"
startswith()
print(s.startswith("Hello"))

endswith()
print(s.endswith("World"))



# counting items

letters = ["P", "Y", "T", "H", "O", "N", "P"]
print(letters.count("P"))



# List Length

letters = ["P", "Y", "T", "H", "O", "N"]
print(len(letters))


# String Length
s = "Hello"

print(len(s))


# Sorting
# Sorting List
letters = ["P", "Y", "T", "H", "O", "N"]

print(sorted(letters))


# String Concatenation
first_name = "   priyanka   "
second_name = " negi   "

# Remove Extra Spaces
first_name = first_name.strip()
second_name = second_name.strip()

# Join Strings
full_name = first_name + " " + second_name
print(full_name)


# String Slicing (Most Important)
s = "hello world"

# Indexes:

# h e l l o   w o r l d
# 0 1 2 3 4 5 6 7 8 9 10


print(s[7:11])
# Start from index 7
# Go till index 11 (11 not included)


print(s[:5])
# Start from beginning
# Go till index 5 (not included)


# Common Slicing Patterns
s = "hello world"
Code	Output
s[:5]	hello
s[6:]	world
s[0:5]	hello
s[-5:]	world
s[::-1]	dlrow olleh



# Reverse a String
s = "hello"
print(s[::-1])

# [start : end : step]
