# Lab 3
# Question 4
# Rojan Jafarnezhad
mondayClass = {"Alice", "Bob", "Charlie", "Diana"}
wednesdayClass = {"Bob", "Diana", "Eve", "Frank"}

mondayClass.add("Grace")

print("Monday Class: ", mondayClass)
print("Wednesday Class: ", wednesdayClass)
print("Attended both classes: ", mondayClass&wednesdayClass)
print("Attended either classes: ", mondayClass|wednesdayClass)
print("Only Monday: ", mondayClass-wednesdayClass)
print("Only one class (not both): ", mondayClass^wednesdayClass)
print("Is Monday subset of all students? ", mondayClass <(mondayClass|wednesdayClass))