import math


def distance(p1, p2):
    d1 = p1[0] - p2[0]
    print d1

    d2 = p1[1] - p2[1]
    print d1

    s1 = d1 ** 2
    print s1

    s2 = d2 ** 2
    print s2

    t = s1 + s2
    print t

    d = math.sqrt(t)

    return d


def distance2(p1, p2):
    return math.sqrt(((p1[0] - p2[0]) ** 2) + ((p1[1] - p2[1]) ** 2))


print distance([3.5, 3.5], [5.5, 5.5])
print distance2([3.5, 3.5], [5.5, 5.5])

locations = [
    [5, 5],
    [2, 5],
    [2, 6],
    [1, 4],
    [7, 7],
]
current = [7, 6]


def find_nearest(current, locations):
    best = None
    best_index = 0

    for index in range(0, len(locations)):
        item = locations[index]

        d = distance2(item, current)

        if best is None or d < best:
            best = d
            best_index = index

        index += 1
    return [best_index, best]


result = find_nearest(current, locations)

print result


def print_grid(n):
    output = ""
    for x in range(0, n):
        for y in range(0, n):

            if current[0] == x and current[1] == y:
                output += " x"
            # elif isStarbucks():
            #     output += " *"
            else:
                output += " ."

        output += "\n"

    print output


print_grid(10)

# what is the shortest path from the current location to visit all,
#  and then return to the start.
