def fibonacci(limit):
    num1 = 1
    num2 = 1
    print(num1)
    while num2<=limit:
        print(num2)
        newNum = num1 + num2
        num1 = num2
        num2=newNum
        

fibonacci(100)
