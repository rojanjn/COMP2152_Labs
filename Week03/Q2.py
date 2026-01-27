# Lab 3 
# Question 2
# Rojan Jafarnezhad
cart = ["apple", "banana", "milk", "bread", "apple", "eggs"]

print("Number of apples: ", cart.count("apple"))
print("Position of milk: ", cart.index("milk"))

cart.remove("apple")

print("Removed item using pop: ", cart.pop(-1))

if "banana" in cart:
    print("Is banana in cart? True")
else:
    print("Is banana in cart? False")

print("Final cart: ", cart)