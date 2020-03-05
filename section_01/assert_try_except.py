def add_them_up(numbers):
    total = 0
    for n in numbers:
        total = total + n
    return total

print( "Trying" )
total = add_them_up([100, 20, 3, 2])
print("TOTAL:", total)

connected = False

while not connected:
    try:
        assert 121 == total
        print( "Succeeded" )
        connected = True
    except:
        print( "Failed" )

print("yay!")

# import keyword
# print(keyword.kwlist)