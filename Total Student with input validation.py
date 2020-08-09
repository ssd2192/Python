#This program calculate the numbers of students with while loop and input Validation

#the main function
def main():
    endProgram, totalScore, averageScores, score, number, counter = declareVariable()

    while endProgram == "no":
        declareVariable()
        number = getNumber()
        totalScore = getScores(number,totalScore)
        averageScores = getAverage(totalScore, number)
        printAverage(averageScores)
        endProgram = input("Do you want to endd the program?(Enter no to process a new set of test score")
        while not (endProgram == 'yes' or endProgram == 'no'):
            print('please enter a yes or no')
            endProgram = input('do you want to end program? (enter no or yes): ')

def declareVariable():
    endProgram = "no"
    totalScore = 0.0
    averageScores = 0.0
    score = 0
    number = 0
    counter = 1
    return endProgram, totalScore, averageScores, score, number, counter

def getNumber():
    number = int(input("How many students took the test"))
    while number<2 or number >30:
        print("Please enter number between 2 and 30 - Try again")
        number = int(input("How many students took the test"))
    return number

def getScores(number,totalScore):
    counter = 1
    while counter <= number:
        score = int(input("Enter the score"))
        while score<0 or score>100:
            score = int(input("Enter Score between 0 to 100"))
        totalScore += score
        counter += 1
    return totalScore

def getAverage(totalScore, number):
    averageScore = totalScore/number
    return averageScore

def printAverage(averageScores):
    print("The average Score is ", averageScores)
#calls main
main()
