#This program calculate tip, tax and total cost
#This program uses funtions and if conditions

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

#this function will calculate tip for different meal prices
def calc_tip(mealprice):
    if mealprice >= .01 and mealprice <= 5.99:
        tip = mealprice * .10
    if mealprice >= 6 and mealprice <= 12.00:
        tip = mealprice * .13
    if mealprice >= 12.01 and mealprice <= 17.00:
        tip = mealprice * .16
    if mealprice >= 17.01 and mealprice <= 25.00:
        tip = mealprice * .19
    if mealprice >= 25.01:
        tip = mealprice * .22
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
