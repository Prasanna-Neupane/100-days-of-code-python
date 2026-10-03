import tuple, time
print(tuple.name)
print(tuple.num)
print(tuple.tup)
print(time.localtime())
start = time.time()
tame = 0
for i in tuple.tup:
    
    time.sleep(i)
    print("the output was delayed by", i, "seconds")
    tame = tame+i

end = time.time()
print("the total calculated time is ", tame)
print("Total it took", (end-start),"seconds to complete this delayed loop")

print(time.strftime("%H"))

for i in range(30):
    time.sleep(1)
    print("time:", i+1)
                  
import time

for i in range(30):
    print(f"\rTime: {i + 1}", end="", flush=True)
    time.sleep(1)