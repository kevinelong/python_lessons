# While and For loops are used to repeat the code blocks they contain.
#  these indented code blocks are simply one or more lines of code

# The While statement repeats a block of code until,
#  the supplied expression returns false

# Count down from five to zero
my_count = 5
while my_count >= 0:
    print my_count
    my_count = my_count - 1

# A For loop typically repeats a block of code a specific number of times.
# In python they usually loop through items in a list.
# Copying each value from the list in turn into the temporary vaiable specified,
#  before repeating the contained code block.
for fruit in ["Apple", "Orange", "Pear"]:
    print fruit

# Count up from zero to five by generating a list of numbers to loop through.
for n in range(0, 6):
    print n
