import time
timestamp = time.strftime("%H:%M:%S")  #strftime= string format time
print(timestamp)
hour = time.strftime("%H")
print("Hour is", hour)
minute = time.strftime("%M")
print("Minute is", minute)
second = time.strftime("%S")
print("Second is", second)

hour = int(hour)
if(hour<=11):
    print("Good Morning sir.")
elif(hour>11 and hour<=17):
    print("Good Afternoon sir")
elif(hour>=17 and hour<24):
    print("Good Evening Sir")
else:
    print("NONE")

