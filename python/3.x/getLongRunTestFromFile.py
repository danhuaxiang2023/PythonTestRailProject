
inputFile = "C:\\Users\\dxiang\\Downloads\\baas___smoke___automation___68.csv"
outputFile = "C:\\Users\\dxiang\\Downloads\\longrunning___wmmc___milestone_165___adhoc.csv"
longRunTestList = []

with open(inputFile,'r', encoding="UTF-8") as f:
    lines = f.readlines()
    print(lines[0])
    
    # print(type(lines[0]))
    longRunTestList.append(lines[0])
    
    for line in lines[1:]:
        items = line.split(',')
        elapsed = items[2]  # confirm the elaspsed column
        print(elapsed)
        length = len(elapsed.strip()) #  GBOS elapsed without ""
        if length > 2:        

            index = length - 2  # Legaccy/GSS elapsed with ""
            # # print(elapsed[1:length])
            duration = int(elapsed[1:index])       

            # duration = int(elapsed.replace('s','').strip())
            
            print(duration)
            if duration > 300 :
                longRunTestList.append(line)

print(longRunTestList)

with open(outputFile,'a',encoding="UTF-8") as f:
    for row in longRunTestList:
        f.writelines(row)