# string methods by cs50P

#to remove the whitespace. means just the front and back spaces.
name = "           prasanna neupane  "
print(name)
name = name.strip()
print(name)

print(f"hello, my name is {name}")

#to capitalize the first letter. 

fullname = "prasanna neupane".capitalize()
print(fullname)

full_name = "hari yadav"
full_name = full_name.capitalize()

print(full_name)

#to capitalize each word

fake = "prasanna neupane".title()
country = "united kingdom".title()

print(f"my name is {fake} and i live in {country}", end=".\n")

#combined version of all the string method

nume = "prasanna neupane".strip().capitalize()
countries = "united kingdom".strip().capitalize()


#other string methods
#split
hero = "prasanna neupane"
hi = hero.split("a")
print(hi)