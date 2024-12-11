def string_reverse(s):
    """
    Task 1
    - Create a function that reverses a given string (s).
    - s must be a string.
    - Return the reversed string.
    """
    if not type(s) is str:
        raise ValueError("Input must be a string.")
    
    return s[::-1]

# Task 2
# Invoke the function "string_reverse" using the following scenarios:
# - "Hello World"

output1 = string_reverse("Hello World")
print("Reversed string:", output1)


# - "Python"
output2 = string_reverse("Python")
print("Reversed string:", output2)
