def main():
    endProgram = 'no'
    while endProgram == "no":
        notGreenCost = [0] * 2
        goneGreenCost = [0] * 2
        savings = [0] * 2

        months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October',
                  'November', 'December']
        getNotGreen(notGreenCost, months)
        getGoneGreen(goneGreenCost, months)
        energySaved(notGreenCost, goneGreenCost, savings)
        displayInfo(notGreenCost, goneGreenCost, savings, months)
        endProgram = input("do you want to end program? yes or no")
        while endProgram!="no" and endProgram!="yes":
            endProgram = input("do you want to end program? yes or no")


def getNotGreen(notGreenCost, months):
    counter = 0
    while counter < 2:
        notGreenCost[counter] = float(input("Enter NOT GREEN energy costs for " + months[counter] + " "))
        counter = counter + 1
    return getNotGreen


def getGoneGreen(goneGreenCost, months):
    counter = 0
    while counter < 2:
        goneGreenCost[counter] = float(input("Enter GONE GREEN energy costs for " + months[counter] + " "))
        counter = counter + 1
    return goneGreenCost


def energySaved(notGreenCost, goneGreenCost, savings):
    for counter in range(2):
        savings[counter] = notGreenCost[counter] - goneGreenCost[counter]
    return savings


def displayInfo(notGreenCost, goneGreenCost, savings, months):
    counter = 0
    while counter < 2:
        print ("Information for", months[counter])
        print ("savings $", savings[counter])
        print ("Not Green Costs $", notGreenCost[counter])
        print ("Gone Green Costs $", goneGreenCost[counter])
        counter += 1


main()