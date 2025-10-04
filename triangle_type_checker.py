# Input angles from the user
first_angle = int(input("Please enter the first angle: "))
second_angle = int(input("Please enter the second angle: "))

# Calculate the third angle
third_angle = 180 - (first_angle + second_angle)

# Check for valid triangle
if first_angle <= 0 or second_angle <= 0 or third_angle <= 0:
    print("Error")
elif first_angle == 90 or second_angle == 90 or third_angle == 90:
    print("Right angle triangle")
elif first_angle > 90 or second_angle > 90 or third_angle > 90:
    print("Obtuse triangle")
else:
    print("Acute triangle")
