# Write a function that takes two strings as parameters and searches for one inside the other,
# and returns the index position of where the substring was found.
# Use only string array notation an no built in functions that already perform this task.

haystack = "Now is the time for all good people to come to the aid of their party."
needle = "is the"


def index_of_string_in_string(needle, haystack):
    index = 0

    # Your code here.

    # Return -1 if not found.
    return -1


result = index_of_string_in_string(needle, haystack)
print result
assert result == 4
