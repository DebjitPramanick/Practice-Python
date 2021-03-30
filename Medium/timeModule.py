import time


initial = time.time()
k = 0

while(k<5):
    time.sleep(1)
    print("Hello, Debjit here.")
    k+=1

print("While loop ran in ", time.time() - initial)


l1 = time.time()
l2 = time.localtime(l1)
locatime = time.asctime(l2)
print(l1)
print(l2)
print(locatime)
