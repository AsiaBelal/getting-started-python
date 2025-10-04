# input two numbers
x = int(input("Enter the first number (x): "))
y = int(input("Enter the second number (y): "))

# Check if x is a multiple of y and print the result
if y != 0 and x % y == 0:
    print("Yes, the number x is divisible by y")
else:
    print("No")
