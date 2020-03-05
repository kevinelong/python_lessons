# Write a function that takes two strings as parameters and searches for one inside the other,
# and returns the index position of where the substring was found.
# Use only string array notation an no built in functions that already perform this task.

haystack = "Now is the time for all good people to come to the aid of their party."
# needle = "good people"
needle = "is the"


def index_of_string_in_string(needle, haystack):
    index = 0
    while index < len(haystack):
        inner_index = 0
        while inner_index < len(needle) and (index + inner_index) < len(haystack):
            if needle[inner_index] != haystack[index + inner_index]:
                break
            if inner_index == len(needle) - 1:
                return index
            inner_index += 1
        index += 1
    return -1


result = index_of_string_in_string(needle, haystack)
print(result)
assert result == 4
