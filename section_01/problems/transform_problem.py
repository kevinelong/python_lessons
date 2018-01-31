# convert a list of dictionaries into a dictionary of dictionaries
# this is often done so yuo can look up data quickly by a specific key
# like an id

input_data = [
    {
        "id_number": 1001,
        "first_name": "Kevin",
        "last_name": "Long"
    },
    {
        "id_number": 2002,
        "first_name": "John",
        "last_name": "Parker"
    }
]

expected_result = {
    1001: {
        "first_name": "Kevin",
        "last_name": "Long"
    },
    2002: {
        "first_name": "John",
        "last_name": "Parker"
    }
}


def transform(data_list, master_key):
    output = dict()

    # Your code here

    return output


result = transform(input_data, "id_number")
print result
assert result == expected_result
