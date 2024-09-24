import datetime

date_str = input("Enter a date in the format of 'YYYY-MM-DD': ")

try:
    date_formatted = datetime.datetime.strptime(date_str, "%Y-%m-%d")
except ValueError:
    print("Invalid date format. Please try again.")

year = date_formatted.year
month = date_formatted.month
day = date_formatted.day

print(f"Year: {year}, Month: {month}, Day: {day}")