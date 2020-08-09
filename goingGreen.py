# Going Green
# This program calculates the saving base on given values of gas used

def main():
    endProgram = 'no'

    while endProgram == 'no':

        # declare variables
        notGreenCost = [0] * 12
        goneGreenCost = [0] * 12
        savings = [0] * 12
        months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October',
                  'November', 'December']

        #Calling function
        getNotGreen(notGreenCost, months)
        getGoneGreen(goneGreenCost, months)
        energySaved(notGreenCost, goneGreenCost, savings)
        displayInfo(notGreenCost, goneGreenCost, savings, months)
        endProgram = input('Do you want to end program? (Enter no or yes): ')
        while not (endProgram == 'yes' or endProgram == 'no'):
            print ('Please enter a yes or no')
            endProgram = input('Do you want to end program? (Enter no or yes): ')

#Function to get not green used
def getNotGreen(notGreenCost, months):
    counter = 0
    while counter < 12:
        print('Enter NOT GREEN energy costs for', months[counter])
        notGreenCost[counter] = int(input('Enter now -->'))
        counter = counter + 1
    print ('-------------------------------------------------')

#Function to get gone green used
def getGoneGreen(goneGreenCost, months):
    print()
    counter = 0
    while counter < 12:
        print ('Enter GONE GREEN energy costs for', months[counter])
        goneGreenCost[counter] = int(input('Enter now -->'))
        counter = counter + 1
    print ('-------------------------------------------------')

#Function to calculate energy used
def energySaved(notGreenCost, goneGreenCost, savings):
    counter = 0
    while counter < 12:
        savings[counter] = notGreenCost[counter] - goneGreenCost[counter]
        counter = counter + 1

#Function to calculate display results
def displayInfo(notGreenCost, goneGreenCost, savings, months):
    counter = 0
    print()
    print('                        SAVINGS                      ')
    print ('_____________________________________________________')
    print ('SAVINGS     NOT GREEN     GONE GREEN       MONTH')
    print('_____________________________________________________')
    while counter < 12:
        print
        print(
        '$', savings[counter], '         $', notGreenCost[counter], '         $', goneGreenCost[counter], '         ',
        months[counter])
        counter = counter + 1
    print

#Calling main
main()