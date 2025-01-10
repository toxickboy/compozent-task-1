def is_palindrome(s):
    # Remove spaces and make the string lowercase
    s = s.replace(" ", "").lower()
    
    # Compare the string with its reverse
    return s == s[::-1]

# Take input from the user
input_string = input("Enter a string to check if it's a palindrome: ")

# Check if the input string is a palindrome
if is_palindrome(input_string):
    print("The string is a palindrome!")
else:
    print("The string is not a palindrome.")
