"""This program demonstrate how to use variables and functions"""

#This program uses funtions and variables

#the main function
def main():
    print('Welcome tho the tip calculator program')
    print() #Print a blank statement
    mealprice=input_meal()
    tip = calc_tip(mealprice)
    tax = calc_tax(mealprice)
    total = calc_total(mealprice,tax,tip)
    print_info(mealprice,tip,tax,total)

#this funtion will inputs meal price
def input_meal():
    mealprice=float(input("Enter the meal price $"))
    return mealprice

#this function will calculate tip at 20%
def calc_tip(mealprice):
    tip = mealprice * .20
    return tip

#this function will calculate tax at 6%
def calc_tax(mealprice):
    tax= mealprice * .06
    return tax

#this function will calculate tip, tax, and the total cost
def calc_total(mealprice,tax,tip):
    total = mealprice + tax + tip
    return total

#this function will print tip, tax, the mealPrice and the total
def print_info(mealprice,tip,tax,total):
    print("The meal price is $", mealprice)
    print("The tip is $", tip)
    print("The tax is $", tax)
    print("The total is $", total)

#calls main
main()
