# Input number of units
units = int(input("Enter the number of units consumed: "))

# Initialize the bill amount
bill = 0

# Calculate the bill
if units > 400:
    bill += (units - 400) * 10
    units = 400
if units > 200:
    bill += (units - 200) * 10
    units = 200
if units > 100:
    bill += (units - 100) * 5
    units = 100

if bill == 0:
    print("No charge")
else:
    print("The electricity bill for the consumed units", bill)
