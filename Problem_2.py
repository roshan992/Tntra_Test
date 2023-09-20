def is_palindrome(input_str):
    # Remove spaces and convert to lowercase
    input_str = input_str.replace(" ", "").lower()
    
    # Check if the string is equal to its reverse
    return input_str == input_str[::-1] 

user_input = input("Enter a string: ")


if is_palindrome(user_input):
    print("Output: true")
else:
    print("Output: false")
