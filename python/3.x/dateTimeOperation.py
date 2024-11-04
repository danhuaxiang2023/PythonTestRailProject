from pytimeparse.timeparse import timeparse
import datetime
from datetime import datetime
from datetime import timedelta
import time


def convertToUnixTime(date_before):
    #DateTime Format:  '%d/%m/%y %H:%M:%S.%f'
    datetime_object = datetime.strptime(date_before, '%Y-%m-%d %H:%M:%S')
    # print("date_time =>", datetime_object)

    # displaying unix timestamp after conversion
    # print("unix_timestamp => ",
    #       (time.mktime(datetime_object.timetuple())))
    unixtime = int(time.mktime(datetime_object.timetuple()))
    return unixtime


# print( convertToUnixTime('2024-01-14 18:48:00'))


# Convert '1h 4m 9s' format to seconds
def convertToSeconds(elapsed):
    # elapsed = '6w 5h 16'
    wIndex = 0
    hIndex = 0
    mIndex = 0
    sIndex = 0
    week = 0
    hour = 0
    minute = 0
    second = 0

    if 'w' in elapsed or 'd' in elapsed:
        return 10000

    try:
        hIndex = elapsed.index('h')
        # print(f"h Index: {hIndex}")
    except ValueError as e:
        # print("No Hour Found")
        pass

    try:
        mIndex = int(elapsed.index('m'))
        # print(f"m Index: {mIndex}")
    except ValueError as e:
        # print("No Minute Found") 
        pass

    try:
        sIndex = int(elapsed.index('s'))
        # print(print(f"s Index: {sIndex}"))
    except ValueError as e:
        # print("No Second Found")    
        pass 

    if hIndex > 0 and mIndex > 0 and sIndex > 0:
        # print(1)
        hour = int(elapsed[0:hIndex])
        minute = int(elapsed[hIndex+1:mIndex])
        second = int(elapsed[mIndex+1:sIndex])
    elif mIndex > 0 and sIndex > 0:
        # print(2)
        minute = int(elapsed[0:mIndex])
        second = int(elapsed[mIndex+1:sIndex])
    elif mIndex > 0 and sIndex == 0:
        # print(3)
        minute = int(elapsed[0:mIndex])
    elif sIndex > 0:
        # print(4)
        second = int(elapsed[0:sIndex])   

    # print(f"{hour}:{minute}:{second}")
    totalSeconds = hour * 3600 + minute * 60 + second
    # print(f"TotalSeconds: {totalSeconds}s")
    return totalSeconds

if __name__ == "__main__" :
    # elapsed = '6w 5h 16'
    # seconds = convertToSeconds(elapsed=elapsed)
    # print(seconds)

# 'created_on': 1724398274
   unixToDatetime = datetime.fromtimestamp(1724398274) 
   print(unixToDatetime)