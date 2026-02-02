import time

print("Timer starts now ")

timeup=5
for i in reversed(range(0,timeup)):
    seconds= i%60
    minute= int(i/60)%60
    hour = int(minute/3600)%24
    print(f"{hour:02}:{minute:02}:{seconds:02}")
    time.sleep(1)

print("TIME'S UP")






# time.sleep(5)
# print("\nTIME'S UPP!")

