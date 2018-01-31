# Define a function that takes string as a parameter and returns it in reverse
# Use only basic python no built in functions we have not already used.


def reverse(text):
    output = ""
    # ... put your code here
    index = len(text) - 1
    while index >= 0:
        output += text[index]
        index -= 1
    return output


# call the function and store the result
result = reverse("ABC")
print result

# test the result
assert result == "CBA"
