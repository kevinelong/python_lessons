# compare two sequences of characters and rate how similar they are
# based on the number of recurring fragments (words).

# extra credit:
#  compare a master against a list of named items
#  compare each item in a a set against every other item (avoiding self comparisons)


def get_word_counts(text):
    output = {}
    word_list = text.split(" ")

    # Your coded here.

    return output


def get_similarity_score(a, b):
    score = 0

    a_counts = get_word_counts(a)
    b_counts = get_word_counts(b)

    # Your coded here.

    return float(score) / float(possible)


# def compare_items_to_master(master, items):
#     # Your coded here.
#
#
# def compare_each_to_every(items):
#     # Your coded here.
#

master = "Now is the time for all good people to come to the aid of their planet"

items = {
    "A": "The quick brown fox jumped over the lazy dog",
    "B": "Now is the time for all good people to come to the aid of their planet",
    "C": "Turkey is a god",
    "D": "God is a turkey",
    "E": "Apple orange pear turkey",
    "F": "Apple orange pear cherry banana"
}

print get_similarity_score("people are good", master)

compare_items_to_master(master, items)
compare_each_to_every(items)
