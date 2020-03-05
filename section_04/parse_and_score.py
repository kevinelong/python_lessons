
values = {
    "apple":10,
    "orange":20,
    "pear":30,
    "banana": -10,
    "tomato": -50
}

sentence = "Today I ate and apple and a tomato."

words = sentence.split(" ")

total = 0

for w in words:
    if values.has_key(w):
        total = total + values[w]

print(total)
