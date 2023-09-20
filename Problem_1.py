# NOTE : i thinks that second test case have some mistake ive done code according to me

def count_occurrences(input_string, target_character):
    count = 0
    for char in input_string:
        if char == target_character:
            count += 1
    return count

# Get user input for the string and character
input_str = input("Enter a string: ")
target_char = input("Enter a character to count: ")

# Call the function to count occurrences
result = count_occurrences(input_str, target_char)

# Display the result
print(f"Count character '{target_char}' in '{input_str}': {result}")
