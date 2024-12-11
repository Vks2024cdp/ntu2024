def find_first_negative(lst):
    """
    Task 1
    - Create a function that finds the first negative number in a list (lst).
    - Return the first negative number if found, otherwise return "No negatives".
    - Use a while loop to implement this.
    """
    # Ensure the input is a list
    if not isinstance(lst, list):
        raise ValueError("Input must be a list.")

    index = 0
    
    while index < len(lst):
        if lst[index] < 0:  
            return lst[index]
        index += 1  

    return "No negatives"

# Task 2
# Invoke the function "find_first_negative" using the following scenario:
# - [3, 5, -1, 7, -2, 8]

output1 = find_first_negative([3, 5, -1, 7, -2, 8])
print("First negative:", output1)

# - [2, 10, 7, 0]
output2 = find_first_negative([2, 10, 7, 0])
print("First negative:", output2)
