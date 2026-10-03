#Just revising the methods of strings, lists, tuples and dictionaries.
print("revising the methods of strings, lists, tuples and dictionaries")

print("="*20 + "strings"+ "="*20)
name = "   prasanna neupane is the best person in the world.     ..."
address = "he is currently living in some country as my identity is un known and shouldn't be known by many people."

print(f".upper() == {name.upper()}")
print(f".lower() == {name.lower()}")
print(f".title() == {name.title()}")
print(f".capitalize() == {name.capitalize()}")
print(f".strip == {name.strip()}")
print(f".replace == {name.replace("neupane", "rai")}")

print(name)
print(f".find == {name.find("neupane")}")
print(f".count(neupane) == {name.count("neupane")}")
print(f".count(a) == {name.count("a")}")
print(f".isalpha() == {name.isalpha()}")
print(f".isdigit() == {name.isdigit()}")

print("now lets talk about the slicing and position of the string. ")
print(name[:].capitalize())
print(address[0])
print(address[0:4])
print(address[-1])
print(address[-2:-1])
if "prasanna" in name:
    print("found it")

print(address.split(" "))
new = address.split(" ")
print(", ".join(new))


print("="*20 + "List"+ "="*20)

names = ["santosh", "prasanna", "jasbin", "hero", "villain", "proton"]
addresses = ["kagoshori Maitighar", "saint paris", "miami", "switzerland", "australia"]
print(names[:])
print(names[0:3])
print(names[-3:-1])
if "prasann" in names:
    print("it is there.")
else:
    print("it is not there")

print(f".append == {names.append("appended word")}")
print(f".insert == {names.insert(2, "Inserted word in position 2")}")
print(f".extend == {names.extend(["extended 1", "extended 2"])}")
print(addresses.remove("miami"))
print(addresses)

print("="*20 + "tuple"+ "="*20)
print("its about the tuple pack and tuple unpack")

tuples = "prasanna", 21, "S11", "neupane"
namies, roll, section, surname = tuples
print(namies, roll, section, surname)
