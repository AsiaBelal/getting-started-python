month_number = int(input("Enter a number from 1 to 12: "))

if month_number == 1:
    month_name = "January"
    days = 31
elif month_number == 2:
    month_name = "February"
    days = 28
elif month_number == 3:
    month_name = "March"
    days = 31
elif month_number == 4:
    month_name = "April"
    days = 30
elif month_number == 5:
    month_name = "May"
    days = 31
elif month_number == 6:
    month_name = "June"
    days = 30
elif month_number == 7:
    month_name = "July"
    days = 31
elif month_number == 8:
    month_name = "August"
    days = 31
elif month_number == 9:
    month_name = "September"
    days = 30
elif month_number == 10:
    month_name = "October"
    days = 31
elif month_number == 11:
    month_name = "November"
    days = 30
elif month_number == 12:
    month_name = "December"
    days = 31
else:
    month_name = "Invalid month"
    days = 0

print("Month name:", month_name)
print("Days:", days)
