##
# Functions: functions in python are defined using the "def" keyword.
# defining a function gives a name to a series of instructions,
# but does not execute the instructions until later called using the name defined.
# functions may receive a list of variables known as arguments
# the function definition indicates how many are expected,
#  and what each in turn will be named
##


def add(a, b):
    return a + b


# functions once defined must called by name to execute them.
# the series of values passed into a function are called parameters.
# A function can be called once or many times with different parameters

print(add(3, 2))
print(add(7, 9))


# parameters and return values and be of any type

def combine(a, b):
    return a + b

both = combine("bird", "dog")
assert both == "birddog"
print(both)

# the parameters passed in can be variables instead of constants/literals
x = 12
y = 13
#  the result can be stored in a variable
z = add(x, y)
assert z == 25
print(z)


# Functions are a sequence of code instructions you can call by name
#  like a useful formula

def celcius(farenheit):
    output = ((farenheit - 32) * 5) / 9
    return output


print("Farenheit 100 is Celcius " + str(celcius(100)))

# Built in functions - The python language has many built in functions.
# len(text) returns the number of characters in s sstring or quantity of items in a list
# str(n) returns a string representation of a number or object
length = len("word, again")
assert length == 11

converted_length = len(str(3 * 4))
assert converted_length == 2
print(converted_length)
