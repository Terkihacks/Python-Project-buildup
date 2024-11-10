# Tuples - Similar to list but placed in paranthesis
# But tuples are immutable
# eg var = ("hello")
students = ("Lynne","Xabisa","Milka","Baluba",4,True)
# Accesing Tuples with index
print(students[2])
print(type (students))

# Dictionaries are mutable and unordered collection of key-value pairs 
capital_city = {
    "Nepal":"Kathmandu",
    "Nigeria":"Abuja",
    "Kenya":"Nairoberry",
    "South Africa":"Pretoria"
    }
print(capital_city)
print(type(capital_city))
# Accesing Dictionaries
# print(capital_city["Nepal"])

capital_city["Sierra leon"] = "Free Town"
print(capital_city)

# SETS - A collection of unique data and cant be duplicated
 # Sets are mutable and unordered collection of unique elements
 # Sets are used to store multiple items in a single variable
 # Sets are unordered, so we cannot access items by index
 # Sets are mutable, so we can add or remove items

studentsIds = {12,13,14,34,35}
print(studentsIds)
# To order sets we use a method calles sorted()
print(sorted(studentsIds))
# To add items in sets we use add()
studentsIds.add(45)
print(studentsIds)

# ARITHMETIC OPERATORS
# + (Addition)
# - (Subtraction)
# * (Multiplication)
# / (Division)
# % (Modulus)
# ** (Exponentiation)
# // (Floor Division)

# ASSIGNMENT OPERATORS
# = (Assignment)
# += (Addition Assignment)
x=10
x+=3
print(x)
# -= (Subtraction Assignment)
# == (Equal)