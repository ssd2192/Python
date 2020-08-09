#This program calculate the total price
#This program demonstrate for loops

#the main function
def main():

    #A basic for loop
    print("I will display the number 1 through 5.")
    for num in [1,2,3,4,5]:
        print(num)

    #The second counter code
    for counter in range(1,61):
        print(counter)

    #The accumulator code
    total = 0
    for counter in range(5):
        number = int(input("Enter a number: "))
        total += number
    print("The total is ", total)

    #The Average Age code
    totalAge = 0
    averageAge = 0
    number = int(input("How many ages do you want to enter: "))
    for counter in range(0, number):
        age = int(input("Enter an age: "))
        totalAge += age
    averageAge = totalAge/number
    print("The average age is", averageAge)

#calls main
main()
