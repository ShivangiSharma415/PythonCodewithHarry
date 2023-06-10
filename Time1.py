import time
# kisi bhi program ka execution time nikal sakte hai

# time module me ek time function hai jo per second badhta hai,ticks me return krta hai

totaltime= time.time()
print(totaltime)

k = 0
while(k<10):
    print("Hello dunia")
    time.sleep(2)
    k+=1
print("While loop ran in",time.time()-totaltime, "seconds")

localtime = time.asctime(time.localtime(time.time()))
print(localtime)