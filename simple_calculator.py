x = float(input("please enter a num: "))
z = float(input("please enter a num: "))
operator = input("please enter the operators: ")

if operator == '+':
    print("x+z =", x + z)
elif operator == '-':
    print("x-z =", x - z)
elif operator == '*':
    print("x*z =", x * z)
elif operator == '/' and z != 0:
    print("x/z =", x / z)
else:
    print("error")
