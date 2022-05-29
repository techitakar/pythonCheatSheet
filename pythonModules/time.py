import time

print(time.ctime()) #get current Time
gmtTime=time.gmtime() #returns a struct
print(f'GMT TIME: {gmtTime.tm_hour}:{gmtTime.tm_min}:{gmtTime.tm_sec}')

#loop
def printCtime():
    print(time.ctime())

if __name__=="__main__":
    while True:
        printCtime()
        time.sleep(2) #wait in seconds...