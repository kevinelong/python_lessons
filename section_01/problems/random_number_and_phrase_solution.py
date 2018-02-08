import random


def pick_a_number_between(minimum, maximum):
    r = random.randint(minimum, maximum)
    return r


print pick_a_number_between(1, 10)

# PICK RANDOM PHRASE FROM LIST

phrases = [
    "I like apples.",
    "I like oranges.",
    "I like pears."
]


def pick_random_item_from_list(item_list):
    count = len(item_list)
    limit = count - 1
    index = random.randint(0, limit)
    text = item_list[index]

    return text


print pick_random_item_from_list(phrases)

