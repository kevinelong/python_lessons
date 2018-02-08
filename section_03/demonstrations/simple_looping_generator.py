from random import randint

for n in ["STR", "INT", "DEX", "WIS", "CON", "CHA"]:
    output = []
    for d in range(0, 3):
        output.append(randint(1, 6))
    print n, sum(output)
