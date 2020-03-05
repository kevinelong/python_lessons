# ASSIGNMENT:
# use the random package's randint function
my_number = 3
number_guessed = 0

while number_guessed != my_number:
    number_guessed = input("Guess my number (between 1 and 5):")
    number_guessed = int(number_guessed)

print("You are right!")
print("My number was " + str(my_number) + "!")
