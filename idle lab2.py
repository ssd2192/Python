"""This program will take in total sales from the user then
calculate and display the county tax, state tax and total tax"""

#Declaration and calling
def main():
    print('Welcome tho the tax calculator program')
    print() #Print a blank statement
    totalSales=inputData()
    countyTax=calcCounty(totalSales)
    stateTax=calcState(totalSales)
    totalTax=calcTotalTax(countyTax,stateTax)
    printData(countyTax,stateTax,totalTax)

#this funtion will take the total sales as input from user
def inputData():
    totalSales=float(input("Enter Total Sales"))
    return totalSales

#this funtion will calculate the county tax and return value
def calcCounty(totalSales):
    countyTax= totalSales * .02
    return countyTax

#this funtion will calculate the state tax and return value
def calcState(totalSales):
    stateTax=totalSales * .04
    return stateTax

#this funtion will calculate the total tax and return value
def calcTotalTax(countyTax, stateTax):
    totalTax= countyTax + stateTax
    return totalTax

#this funtion will print county tax, state tax and the total tax calculated
def printData(countyTax, stateTax, totalTax):
    print("County Tax", countyTax)
    print("State Tax", stateTax)
    print("Total Tax", totalTax)

main()
