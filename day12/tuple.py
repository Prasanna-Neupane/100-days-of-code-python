tup = (1, 2, 5, 2, 6, 7, 8)
num = (34, 65, 23, 79)
name = ("prasanna", "neupane", "doreamon", "troll", "changes")

if __name__ == "__main__": 
    print(type(tuple), tup, tup[2])

    if 5 in tup:
        print("5 is present.")

    print("methods of tuple")
    combined = name+tup
    print("the combined tuple is ", combined)
    position = combined.index(2)
    count = combined.count(2)
    print(position,",", count)