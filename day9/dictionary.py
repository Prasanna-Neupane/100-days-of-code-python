#for dictionary use {} barckets.
students = {"name": "prasanna",
             "class":12,
               "section": "S11",
                 "roll number":21}

# If i hade to write the things listed above in the LIST method i would write like this which is not good.

category = ["name", "class", "section", "roll number"]
details = ["prasanna", 12, "S11", 21] 
# and somehow make connection between these two variables. 

print("what is his name")
print(f"his name is {students["name"]} and his roll number is {students['roll number']}")
print(category[0])
print("\n list and information of all the students.")
for student in students:
    print(student, " = ", students[student])

#its time for combining the list and dictionary.

lads = [
    {"name": "prasanna neupane", "roll number": 21, "address": "force park"},
    {"name": "sandesh rai", "roll number": 27, "address": "korea"},
    {"name": "jasbin kandel chettri", "roll number": 12, "address": "france"},
    {"name": "abijit gurung", "roll number": 2, "address": None},
    #None means absence of value.
]

print(lads)
print("="*30)
print(lads[0])
for i in lads:
    print(i)
    print(i["name"])
print()
print("lets print all the details more properly from the list of dictionaries. ")
rise= 1
for num in lads:
    
    position = lads.index(lads[rise-1])+1
    nam = num["name"]
    roll = num["roll number"]
    place = num["address"]
    print("The name on the", position, "position is", nam, f"whose roll number is {roll} and he lives in {place}")
    rise+=1