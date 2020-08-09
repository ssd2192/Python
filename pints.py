#Arrays and Python Code
# This program calculates the average pints, high pints and low pints collected

def main():
    endProgram = 'no'
    while endProgram == 'no':
        #Declare Variables
        pints = [0] * 7
        totalPints = 0
        averagePints = 0
        highPints = 0
        lowPints = 0

        #Calling Functions
        pints = getPints(pints)
        totalPints = getTotal(pints, totalPints)
        averagePints = getAverage(totalPints, averagePints)
        highPints = getHigh(pints, highPints)
        lowPints = getLow(pints, lowPints)
        displayInfo(averagePints, highPints, lowPints)

        endProgram = input('\nDo you want to end program? (Enter no or yes): ')
        while not (endProgram == 'yes' or endProgram == 'no'):
            print ("Please enter a yes or no")
            endProgram = input('Dp ypu want to end program? (Enter no or yes): ')

#Function to get Pints
def getPints(pints):
    counter = 0
    while counter < 7:
        pints[counter] = int(input('Enter pints collected: '))
        counter = counter + 1
    return pints

#Function to calculate total pints
def getTotal(pints, totalPints):
    counter = 0
    while counter < 7:
        totalPints = totalPints + pints[counter]
        counter = counter + 1
    return totalPints

#Function to calculate average pints
def getAverage(totalPints, averagePints):
    averagePints = float(totalPints) / 7
    return averagePints

#Calculate highest pint
def getHigh(pints, highPints):
    highPints = pints[0]
    counter = 1
    while counter < 7:
        if pints[counter] > highPints:
            highPints = pints[counter]
        counter = counter + 1
    return highPints

#Calculate lowest pint
def getLow(pints, lowPints):
    lowPints = pints[0]
    counter = 1
    while counter < 7:
        if pints[counter] < lowPints:
            lowPints = pints[counter]
        counter = counter + 1
    return lowPints

#Function to display Results
def displayInfo(averagePints, highPints, lowPints):
    print ("The average number of pints donated is ", averagePints)
    print ("The highest pints donated is ", highPints)
    print ("The lowest pints donated is ", lowPints)

#Call main
main()