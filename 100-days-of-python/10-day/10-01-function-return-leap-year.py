'''
def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                print("Leap year.")
            else:
                print("Not leap year.")
        else:
            print("Leap year.")
    else:
        print("Mot leap year.")


def days_in_month():
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

year = int(input("Enter a year: "))
mounth = int(input("Enter a month: "))
days = days_in_month(year, mounth)
print(days)

'''


def is_leap(year):
    """Take a year and check if it leaf"""
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

def days_in_month(year, month):
    """Take a year and month, and count days in month""" #//это doc-string
    if month > 12 or month < 1:
        return "Invalid month"
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if is_leap(year) and mounth == 2:
        return 29
    return month_days[month -1]

year = int(input("Enter a year: "))
mounth = int(input("Enter a month: "))
days = days_in_month(year, mounth)
print(days)