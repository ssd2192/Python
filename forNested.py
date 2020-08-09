def multTable():

    maxNum = int(input("Enter Max Number: "))
    for row in range(1,maxNum+1):
        print()
        for col in range(1,maxNum+1):
            print(format(row*col,'5d'), ' ')
            
multTable()
