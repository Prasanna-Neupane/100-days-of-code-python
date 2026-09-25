# print("|"+"="*99+"|")
# print(f"| {"base monthly salary".title():<30}| {123456:<30}  | {8765432:<30}  |")
# print(f"| {"overtime hour".title():<30}| {1:<30}  | {8:<30}  |")
# print(f"| {"overtime pay".title():<30}| {1234:<30}  | {876:<30}  |")
# print(f"| {"gross salary".title():<30}| {123433:<30}  | {876098:<30}  |")

# first_hourly_salary = input("what is your hourly salary? ".capitalize())
# first_hour_per_day = input("enter the working hour per day: ")

def monthly_salary(salary):
    day = 8*int(salary)
    month = day *30
    return month

def overtime_hour(time):
    hour = (int(time)-8)*30
    return hour

def overtime_hour_salary(hour, salary):
    day = (int(hour)-8)*int(salary)
    month = day*30
    return month

def gross_salary(hour, salary):
    total = monthly_salary(salary) + overtime_hour_salary(hour, salary)
    return int(total)
