# Sample Coding Questions 01 Week 01
# Rojan Jafarnezhad

# defining variables
array_list = [1, 4, 7, 9]

# order of operations
a = 1
b = 2
c = 3
d = 4

# e = a * c - b / d
# e = (a * c) - (b / d)
# e = a - b ** c // d + a % c
e = a - (b ** (c // d) + (a % c))

# formatting
temprature = 32.6
print(f"The temprature today is: {temprature}")

# common functions
userAge = input("How old are you? 22")
print(f"Now showing the shop items filtered by age: {userAge}")