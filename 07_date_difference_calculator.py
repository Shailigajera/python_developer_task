

"""
Problem:
Calculate the number of days between two given dates.
Scenario:
A user wants to know how many days they have lived based on their birthdate and today's date.

Approach:
- Take two inputs in the format dd-mm-yyyy.
- Convert strings to datetime objects using datetime.strptime.
- Calculate the difference in days using subtraction.
"""

from datetime import datetime

def calculate_date_difference(start_date_str, end_date_str):
    try:
        date_format = "%d-%m-%Y"
        start_date = datetime.strptime(start_date_str, date_format)
        end_date = datetime.strptime(end_date_str, date_format)
        difference = end_date - start_date
        return abs(difference.days)
    except ValueError:
        return None

if __name__ == "__main__":
    birth_date = input("Enter your birthdate (dd-mm-yyyy): ")
    today_date = input("Enter today's date (dd-mm-yyyy): ")
    days = calculate_date_difference(birth_date, today_date)
    if days is not None:
        print(f"\nYou have lived for {days} days.")
    else:
        print("\nInvalid date format. Please use dd-mm-yyyy.")
