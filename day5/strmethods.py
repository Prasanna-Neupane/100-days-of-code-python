real = "   Prasanna neupane@!!!!"

#string methods

print(len(real), "is he length of the original string. ")
print(f"the string in uppercase is {real.upper()}")
print(f"the string in lowercase is {real.lower()}")
print("now showing the feature of strip function")
print(f"removable of whitespaces: {real.strip()}")
print(f"removable of !: {real.strip("!")}")
print(f"removable of @: {real.strip("@")}")
print(f"removing all whitespaces, @ and ! and we get {real.strip().strip("!").strip("@")}")
print(f"removing all whitespaces, @ and ! in more clean way and we get {real.strip(" @!")}")
print("reminder that strip() never remove any characters from the middle of the string")


name = real.strip(" @!").title()
print("replacing the characters")
print(name.replace("Prasanna", "Sandesh"))
print("now spliting the name whereaver there is space and convert them into list")
print(name.split(" "))

print(name.center(60))
print(len(name), "is the length of the normal string")
print(len(name.center(60)), "is the length of the centered string")

print("to know how many characters are there in the string, we generally use count() function")
print("a:" + str(name.count("a")))
print("Prasanna:", name.count("Prasanna"))

print("find() function only operates when there is character in the string. It gives the location of only first characters if there are multiple same characters")
print("p:" ,name.find("p"))
print("Neup:" ,name.find("Neup"))
print("if there is no character than it gives -1")
print(name.find("z"))

print("to identify whether the string is alpanumeric or not. Alpa numeric means (A-Z, a-z, 0-9)")
print("thisfsfERERFAE23456".isalnum())
print("thisfsfERE...RFAE23456".isalnum())
print("to identify the alpha. alpha means (A-Z, a-z)")
print("thisfsfERERFAE".isalpha())
print("thisfsfERERFAE34543".isalpha())