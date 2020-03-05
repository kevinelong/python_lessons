# Conditonal exper

# assign the text value GREEN to variable named light
light = "GREEN"

if light == "GREEN":
    print("Go")
elif light == "RED":
    print("Stop")
elif light == "YELLOW":
    print("Go Very Fast")

age = 19
legal = 21

if age >= legal:
    print("Can Drink")
else:
    print("Can't Drink")

# Additional info links
# https://en.wikipedia.org/wiki/Conditional_(computer_programming)

# Truth table for logical AND
# A B (A and B)
# 0 0 0
# 0 1 0
# 1 0 0
# 1 1 1

# Truth table for logical OR
# A B (A and B)
# 0 0 0
# 0 1 1
# 1 0 1
# 1 1 1

assert not (False and True)
assert not (True and False)
assert not (False and False)
assert (True and True)

can_buy = False

bank_balance = 1
rent_due = True

has_credit_card = True

if bank_balance > 0 and not rent_due:
    can_buy = True

if bank_balance > 0 or has_credit_card:
    can_buy = True

if (bank_balance > 0 and not rent_due) or has_credit_card:
    can_buy = True

if has_credit_card or (bank_balance > 0 and not rent_due):
    can_buy = True
