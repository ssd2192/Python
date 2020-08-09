def totalEmpHrs():
    totalEmpHrs = 0
    empNumber= int(input("Enter Employee # or 0000 to exit"))
    while empNumber!=0000:
        empHours= float(input("Enter Employee Hours"));
        totalEmpHrs += empHours
        empNumber= int(input("Enter Employee # or 0000 to exit"))
    print("Total Employee Hours--->", totalEmpHrs)
    
totalEmpHrs()
