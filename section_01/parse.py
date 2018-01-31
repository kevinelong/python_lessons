

# Define a function
# that takes a string
# and returns an integer
# that represents how many words


def word_count(text):
    space = " "
    words = text.split(space)
    quantity = len(words)
    return quantity


s = "Now is the time..."

c = word_count(s)

print c

# part two
parts = s.split(" ")
print parts[2]

# five things in one line - code golf
print "apple orange pear cherry".split(" ")[2]

print "12,9,3".split(",")[1]
