# Input 
num = input("Enter an integer: ")

# Checking Palindrome ?
if num == num[::-1]:
    print(f"{num} is a palindrome number")
else:
    print(f"{num} is not a palindrome number")
