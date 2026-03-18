s = input("Enter a string: ")

# Palindrome
if s == s[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")

# Symmetrical
mid = len(s) // 2
if s[:mid] == s[mid:]:
    print("Symmetrical")
else:
    print("Not Symmetrical")
