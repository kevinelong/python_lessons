# Write a function that takes string as input,
# and returns a dictionary object,
# where the keys are the characters in the string,
# and the values are the number of times each letter occurs.


def letter_count(text):
    output = dict()

    for c in text:
        if c not in output:
            output[c] = 1
        else:
            output[c] += 1

    return output


result = letter_count("Now is the time for all good people to come to the aid of their planet.")
print result
assert result == {'a': 3, ' ': 15, 'c': 1, 'e': 8, 'd': 2, 'g': 1, 'f': 2, 'i': 4, 'h': 3, 'm': 2, 'l': 4, 'o': 9,
                  'N': 1, 'p': 3, 's': 1, 'r': 2, 't': 7, 'w': 1, '.': 1, 'n': 1}

# EXTRA CREDIT:
# How could you ignore spaces?
# How could you get the largest letter?
# How could you find the number of occurrences of whole words instead of letters?
# How could you return them in order of frequency?
# How else could this be improved or re-purposed?
