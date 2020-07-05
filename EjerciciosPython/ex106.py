"""
Created on Wed Jun 24 19:12:51 2020

@author: fpalm

Write a function that determines how many days there are in a particular month. Your
function will take two parameters: The month as an integer between 1 and 12, and
the year as a four digit integer. Ensure that your function reports the correct number
of days in February for leap years. Include a main program that reads a month and
year from the user and displays the number of days in that month. You may find your
solution to Exercise 58 helpful when solving this problem.

"""

from ex58 import is_leap_year

days_in_month = {
    (4, 6, 9, 11): 30,
    (1, 3, 5, 7, 8, 10, 12): 31,
    (2,): 28
}

def how_many_days(month, year):
    """how many days there are in a particular month and year.

    Parameters
    ----------
    month : int
        month in numeric format.
    year : int
        year in numeric format.

    Returns
    -------
    days : int
        number of days in that month and year. Ensuring that is the correct
        number of days in February for leap years.

    """
    for key in days_in_month.keys():
        if month in key:
            days = days_in_month[key]
            break
    if month == 2:
        days += 1 if is_leap_year(year) else 0
    return days

if __name__ == "__main__":
    month = int(input("month? "))
    year = int(input("year? "))
    days = how_many_days(month, year)
    print(f"month {month} in year {year} has {days} days.")
    