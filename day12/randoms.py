import random
from tuple import name, num, tup

list = (1, 2,3,4, 5)

randoms = random.choice(name)
print(randoms)
hax = random.choice(num)
print(hax)

print(randoms, "loves the number", hax)

print(random.randint(1, 99))