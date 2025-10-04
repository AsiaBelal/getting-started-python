# grade_and_profile_input.py
# ------------------------------------
# Program 1: Student Grade Calculator
# ------------------------------------

# Get grades from the user
chemistry = float(input("Enter your grade in Chemistry: "))
physics = float(input("Enter your grade in Physics: "))
biology = float(input("Enter your grade in Biology: "))
maths = float(input("Enter your grade in Maths: "))
computer = float(input("Enter your grade in Computer: "))

# List of the grades
grades = [chemistry, physics, maths, biology, computer]

# Calculate the average percentage
average_percentage = sum(grades) / len(grades)

# Check if any subject grade is less than 50
has_failing_grade = (
    chemistry < 50 or
    physics < 50 or
    biology < 50 or
    maths < 50 or
    computer < 50
)

# Determine the overall grade
if has_failing_grade:
    overall_grade = 'F'
else:
    if average_percentage >= 90:
        overall_grade = 'A'
    elif average_percentage >= 80:
        overall_grade = 'B'
    elif average_percentage >= 70:
        overall_grade = 'C'
    elif average_percentage >= 60:
        overall_grade = 'D'
    else:
        overall_grade = 'F'

# Print the grades and overall result
print("\n--- Student Grades ---")
print("Chemistry:", chemistry)
print("Physics:", physics)
print("Biology:", biology)
print("Maths:", maths)
print("Computer:", computer)
print("Average Percentage:", average_percentage)
print("Overall Grade:", overall_grade)


# ------------------------------------
# Program 2: User Profile Collector
# ------------------------------------

# Collect user's basic information
print("\n--- Create Your Profile ---")
name = input("Enter your name: ")
age = input("Enter your age: ")
email = input("Enter your email: ")
job = input("Enter your job position: ")

# Display user profile
print("\n--- User Profile ---")
print("Name:", name)
print("Age:", age)
print("Email:", email)
print("Job:", job)
