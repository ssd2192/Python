# Minutes Allowed

def main():
    endProgram = "no"
    # declare varables
    minutesAllowed = 0
    minutesUsed = 0
    totalDue = 0
    minutesOver = 0

    while endProgram == "no":
        # functions/modules
        minutesAllowed = getAllowed(minutesAllowed)
        minutesUsed = getUsed(minutesUsed)
        totalDue, minutesOver = calcTotal(minutesAllowed, minutesUsed, totalDue, minutesOver)
        printData(minutesAllowed, minutesUsed, totalDue, minutesOver)

        endProgram = input('do you want to end program? (enter no or yes): ')
        while not (endProgram == 'yes' or endProgram == 'no'):
            print('please enter a yes or no')
            endProgram = input('do you want to end program? (enter no or yes): ')


# this function will get how many minutes are allowed
def getAllowed(minutesAllowed):
    minutesAllowed = int(input('how many minutes are allowed: '))
    while minutesAllowed < 200 or minutesAllowed > 800:
        print('please enter minutes between 200 and 800')
        minutesAllowed = int(input('how many minutes are allowed: '))
    return minutesAllowed


def getUsed(minutesUsed):
    minutesUsed = int(input('how many minutes were used: '))
    while minutesUsed < 0:
        print('please enter minutes used of at least 0')
        minutesUsed = input('how many minutes were used: ')
    return minutesUsed


# this function will calculate total due
def calcTotal(minutesAllowed, minutesUsed, totalDue, minutesOver):
    if minutesUsed <= minutesAllowed:
        totalDue = 74.99
        minutesOver = 0
        print()
        print('you were not over your minutes for the month')

    elif minutesUsed>minutesAllowed:
        minutesOver = minutesUsed - minutesAllowed
        extra = minutesOver * .20
        totalDue = 74.99 + extra
        print()
        print('you were over your minutes by ', minutesOver)

    return totalDue, minutesOver


# this function display the information
def printData(minutesAllowed, minutesUsed, totalDue, minutesOver):
    print()
    print('--------------------MONTHLY USE REPORT--------------------')
    print()
    print('minutes allowed were', minutesAllowed)
    print('minutes used were', minutesUsed)
    print('minutes over were', minutesOver)
    print('total due is $', totalDue)
    print()

# calls main
main()