def swap(x, y):
    """
    Task 1
    - Create a function that would swap the value of x and y using only x and y as variables.
    - x and y must be numeric.
    - Return -1 if x and y is not numeric, and
    - print the swapped values if both x and y are numeric.
    """

    if not (type(x) in [int, float] and type(y) in [int, float]):
    return -1
    x, y = y, x
    print(f"Swapped values: x = {x}, y = {y}")
    return


# Task 2
# Invoke the function "swap" using the following scenarios:
# - "Apple", 10
output1 = swap("Apple", 10)  
print("output:" , output1)

# - 9, 17
output2 = swap(9, 17) 
print("output2:", output2)
