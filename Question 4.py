def is_leap_year(a_year):
    """Checks input to see if its a leap year and returns a boolean"""

    if a_year % 4 == 0:
        if a_year % 400 == 0:
            return(True)
        elif a_year % 100 == 0:
            return(False)
        else:
            return(True)
    else:
        return(False)

print(is_leap_year(801))