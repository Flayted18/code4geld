"""
Created on Wed Jun 24 18:38:03 2020

@author: fpalm

Most years have 365 days. However, the time required for the Earth to orbit the Sun
is actually slightly more than that. As a result, an extra day, February 29, is included
in some years to correct for this difference. Such years are referred to as leap years.
The rules for determining whether or not a year is a leap year follow:

 * Any year that is divisible by 400 is a leap year.
 * Of the remaining years, any year that is divisible by 100 is not a leap year.
 * Of the remaining years, any year that is divisible by 4 is a leap year.
 * All other years are not leap years.

Write a program that reads a year from the user and displays a message indicating
whether or not it is a leap year.
"""

def is_leap_year(year):
    """
    

    Parameters
    ----------
    year : TYPE
        DESCRIPTION.

    Returns
    -------
    bool
        DESCRIPTION.

    """
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False

if __name__ == "__main__":
    year = int(input("year? "))
    result = is_leap_year(year)
    if result:
        print(f"{year} is a leap year.")
    else:
        print(f"{year} is not a leap year.")

print(__name__)