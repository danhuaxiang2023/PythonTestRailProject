    
elapsed = '4s'
hIndex = 0
mIndex = 0
sIndex = 0
hour = 0
minute = 0
second = 0
try:
    hIndex = elapsed.index('h')
    print(f"h Index: {hIndex}")
except ValueError as e:
    print("No Hour Found")

try:
    mIndex = int(elapsed.index('m'))
    print(f"m Index: {mIndex}")
except ValueError as e:
    print("No Minute Found") 

try:
    sIndex = int(elapsed.index('s'))
    print(print(f"s Index: {sIndex}"))
except ValueError as e:
    print("No Second Found")     

if hIndex > 0 and mIndex > 0 and sIndex > 0:
    print(1)
    hour = int(elapsed[0:hIndex])
    minute = int(elapsed[hIndex+1:mIndex])
    second = int(elapsed[mIndex+1:sIndex])
elif mIndex > 0 and sIndex > 0:
    print(2)
    minute = int(elapsed[0:mIndex])
    second = int(elapsed[mIndex+1:sIndex])
elif mIndex > 0 and sIndex == 0:
    print(3)
    minute = int(elapsed[0:mIndex])
elif sIndex > 0:
    print(4)
    second = int(elapsed[0:sIndex])   

print(f"{hour}:{minute}:{second}")
totalSeconds = hour * 3600 + minute * 60 + second
print(f"TotalSeconds: {totalSeconds}s")