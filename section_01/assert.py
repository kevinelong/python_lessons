def add_them_up(numbers):
    total = 0
    for n in numbers:
        total = total + n
    return total


try:
    print "Trying"
    total = add_them_up([100, 20, 3, 2])
    print "TOTAL:", total

    assert 123 == total
    print "Succeeded"

except:
    print "Failed"

import keyword
print(keyword.kwlist)