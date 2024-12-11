def update_dictionary(dct, key, value):
    """
 #   Task 1
#  - Create a function that updates a dictionary (dct) with a new key-value pair.
#    - If the key already exists in dct, print the original value, then update its value.
 #   - Return the updated dictionary.
  #  """

    if key in dct:
        print(f"Key '{key}' already exists with value: {dct[key]}")
        dct[key] = value
    return dct

# Task 2
# Invoke the function "update_dictionary" using the following scenarios:
# - {}, "name", "Alice"

output1 = update_dictionary({}, "name", "Alice")
print("Updated dictionary:", output1)

# - {"age": 25}, "age", 26
output2 = update_dictionary({"age": 25}, "age", 26)
print("Updated dictionary:", output2)
