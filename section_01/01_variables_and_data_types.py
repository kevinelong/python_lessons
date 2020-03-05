# ##
# VARIABLES AND DATA TYPES
###

# Variable: A named reference to a value.
# Imagine a jar with a label on it,
#  inside the jar is a piece of paper with a value on it.
# e.g. label says "quantity",
#  and the value written on the paper inside the jar says "144"
quantity = 144

print(quantity)

# Data Type: A Specific kind of variable (e.g. Integer, String, List)

# Numbers: numbers come in two flavors

# Integer: whole numbers (e.g. 1,2,3)
i = 12

# Float: A floating-point/decimal number can hold fractional values (e.g. 1.0, 0.25 13.79)
f = 33.33
half = 1.0 / 2.0

# String: An ordered sequence of characters(individual letters or numbers)
student_name = "Alice Jones"

# List: A list is an ordered array of values,
#  that can be referenced by a number know as the index.
#
# 0 is the index of the first item,
# 1 is the second item,
# 2 is the third item, etc
#
# -1 is the last item,
# -2 is the second to the last item

# An empty list and be created two ways

# One way is to use the shorthand of a set of empty square brackets
# e.g.
my_list = []

# Another is to explicitly call the list objects constructor by name
another_list = list()

# you can pass in a comma separated value to be put into the list initially
numbers = [13, 9, 66, 11]

# values can be of any type or even mixed types such as numbers and strings
stuff = ["apple", 13, 6, "banana"]

# You can break it up into multiple lines for clarity
fruit = [
    "apple",
    "orange",
    "pear"
]

people = list("Bob", "Carol", "Ted", "Alice")

# Get the first item in the list
first_person = people[0]

# Get the last item in the list
last_person = people[-1]

quarterly_sales_for_year = [100, 75, 50, 200]
# Get the third item in the list
q3 = quarterly_sales_for_year[2]

# Dictionary: a dictionary is an unordered collection of ,
#  that can be accessed by a name known as a key,
#  like a phone book or library

# A dictionary object can be create with the short curly brace syntax
phone_book = {"Bob": "555-555-2222", "Carol": "555-555-3333", "Ted": "555-555-4444", "Alice": "555-555-1111"}
alice_number = phone_book["Alice"]

# Boolean: A Boolean is a binary logical value. e.g. True or False
is_a_student = True
is_cheating = False
