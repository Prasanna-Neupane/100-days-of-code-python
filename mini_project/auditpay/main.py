import security, pay

title = print("paytrace".upper())
#==========================EMPLOYEE 1===============================================
print("salary of 1st employee")

first_name = str(input("enter your name of first user: ".capitalize()))
first_email = str(input("enter email: ".title()))
first_password = input("enter passoword: ".capitalize())
first_hourly_salary = input("what is your hourly salary? ".capitalize())
first_hour_per_day = input("enter the working hour per day: ")

#============================EMPLOYEE 2=============================================
print("salary of 2nd employee")

second_name = str(input("enter your name of second user: ".capitalize()))
second_email = str(input("enter email: "))
second_password = input("enter passoword".capitalize())
second_hourly_salary = input("what is your hourly salary? ".capitalize())
second_hour_per_day = input("enter the working hour per day: ")
#---------------------------------------------------------------AUDIT REPORT-----------------------------------------------------------------#

print("\n\n")
print("|"+"="*99+"|")
print("|"+"PAYTRACE: DUAL-EMPLOYEE COMPARATIVE AUDIT ".center(99)+"|")
print("|"+"="*99+"|")

print("|"+"policy".center(99).upper()+"|")

print("1. The maximum working hour per day is 8 hours.")
print("2. 13%tax is implemented in the monthly salary.")
print("3. 2% wage is deducted from the salary for provident fund. ")
print("4. The salary is displayed in different curreny.")

#watchmedo auto-restart --patterns="*.py" --recursive -- python main.py
print(f"| {"METADATA":<30}| {"EMPLOYEE #1":<30}  | {"EMPLOYEE #2":<30}  |")
print("|"+"="*99+"|")

print(f"| {"full name".title():<30}| {security.pure(first_name):<30}  | {security.pure(second_name):<30}  |")
print(f"| {"first name".title():<30}| {security.first_name(first_name):<30}  | {security.first_name(second_name):<30}  |")
print(f"| {"last name".title():<30}| { security.last_name(first_name):<30}  | {security.last_name(second_name):<30}  |")
print(f"| {"user name".title():<30}| {"PrasNeu1101":<30}  | {"SanRai9843":<30}  |")
print(f"| {"masked email".title():<30}| {security.email_converter(first_email):<30}  | {security.email_converter(second_email):<30}  |")
print(f"| {"password hidden".title():<30}| {security.hide_password(first_password):<30}  | {security.hide_password(second_password):<30}  |")
print(f"| {"batch iD".title():<30}| {"NeuPras8322":<30}  | {"sandesh2345":<30}  |")

print("|"+"="*99+"|")
print(f"| {"base monthly salary".title():<30}| {pay.monthly_salary(first_hourly_salary):<30}  | {pay.monthly_salary(second_hourly_salary):<30}  |")
print(f"| {"overtime hour".title():<30}| {pay.overtime_hour(first_hour_per_day):<30}  | {pay.overtime_hour(second_hour_per_day):<30}  |")
print(f"| {"overtime pay".title():<30}| {pay.overtime_hour_salary(first_hour_per_day, first_hourly_salary):<30}  | {pay.overtime_hour_salary(second_hour_per_day, second_hourly_salary):<30}  |")
print(f"| {"gross salary".title():<30}| {pay.gross_salary(first_hour_per_day, first_hourly_salary):<30}  | {pay.gross_salary(second_hour_per_day, second_hourly_salary):<30}  |")

print("|"+"="*99+"|")
print(f"| {"income tax".title():<30}| {1643:<30}  | {8764:<30}  |")
print(f"| {"provident fund".title():<30}| {502:<30}  | {873:<30}  |")
print(f"| {"total deduction".title():<30}| {2002:<30}  | {9503:<30}  |")

print("|"+"="*99+"|")
print(f"| {"net salary".upper():<30}| {3454:<30}  | {8760:<30}  |")
print(f"| {"USD Equivalent":<30}| {1234:<30}  | {832:<30}  |")
print("|"+"="*99+"|")


print("|"+"comparitive summary".center(99).upper() + "|")
print("|"+"="*99+"|")

print(f"{"|"}+{"absolute pay difference".title():<30}: {3456543:<66}{"|"}")
print(f"{"|"}+{"salary ratio (Emp1 / Emp 2)".title():<30}: {987678:<66}{"|"}")
print(f"{"|"}+{"total company outflow (Both)".title():<30}: {987678:<66}{"|"}")
print(f"{"|"}+{"total tax collected (Both)".title():<30}: {987678:<66}{"|"}")
print("|"+"="*99+"|")
