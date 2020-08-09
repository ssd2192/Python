"""This program demonstrate how to use variables and functions"""

#This program uses funtions and variables

#the main function
def main():
    print('Welcome to the variable program')
    print() #Print a blank statement
    name=inputName()
    age = inputAge()
    print("Hello", name)
    print("Your age is", age)

#this funtion inputs name
def inputName():
    name=input("Enter your name:")
    return name

#this function inputs age
def inputAge():
    age = int(input("Enter your name:"))
    return age

main()
