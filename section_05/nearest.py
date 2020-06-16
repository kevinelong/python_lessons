from math import sqrt, hypot

data = [[531, 408, 'A'], [225, 52, 'B'], [594, 242, 'C'], [351, 102, 'D'], [371, 15, 'E'], [569, 353, 'F'],
        [342, 39, 'G'], [218, 304, 'H'], [428, 260, 'I'], [329, 158, 'J'], [585, 530, 'K'], [71, 114, 'L'],
        [587, 88, 'M'], [347, 180, 'N'], [180, 332, 'O'], [250, 522, 'P'], [88, 475, 'Q'], [260, 128, 'R'],
        [328, 505, 'S'], [381, 201, 'T'], [360, 192, 'U'], [414, 313, 'V'], [525, 293, 'W'], [240, 563, 'X'],
        [117, 546, 'Y'], [507, 127, 'Z']]
square_size = 610
style = """
<style>
    #box { background:blue; position:relative; }
    #box span { color:silver; position:absolute; }
</style>
"""


def distance(p1, p2):
    # return (sqrt( (p2[0] - p1[0])**2 + (p2[1] - p1[1])**2 ))
    return (hypot(p2[0] - p1[0], p2[1] - p1[1]))


letter_dict = {}
for d in data:
    letter = d[2]
    letter_dict[letter] = d


# for arbitrary value e.g. "J" find the nearest N items e.g. 5
def get_top(letter, top_n):
    selected = letter_dict[letter]
    for v in letter_dict.values():
        v.append(distance(v, selected))
    s = sorted(data, key=lambda i: i[3])
    return s[0:top_n + 1]


top = get_top("V", 5)
f = open("positions.html", "w")
f.write(style)
f.write('<div id="box" style="width:{0}px;height:{0}px;">\n'.format(square_size))
for item in data:
    if item in top:
        c = "color:yellow;"
    else:
        c = ""
    f.write('<span style="left:{left}px; top:{y}px;{c}"> {v} </span>'.format(left=item[0], y=item[1], v=item[2], c=c))

f.close()
