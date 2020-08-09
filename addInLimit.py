def addNums(startNum, endNum):
    total = 0
    count = 0
    aNum=startNum
    for aNum in range(startNum, endNum+1):
        total+=aNum
        count+=1
    print(total, count)
addNums(1,5)
