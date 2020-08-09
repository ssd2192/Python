def showMenu():
    print("Employee record Menu")
    print()
    print("1. Search Employee")
    print("2. Add Employee")
    print("3. Delete Employee")
    print()

    menuChoice = int(input("Enter menu Choice: "))
    while menuChoice < 1 or menuChoice > 3:
        menuChoice = int(input("Enter Valid menu Choice: "))

    print("User Made Valid Choice", menuChoice)
        
    
showMenu()
