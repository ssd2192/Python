#Declaration and Input
studnetName = input('Enter student name ')
degreeName = input('Enter degree name ')
creditsTaken = input('Enter Credits Taken ')
creditsDegree = input('Enter total no of credits required in the degree')

#Calculate credits neened to graduate
creditsLeft=int(creditsDegree) - int(creditsTaken);

#Display output
print("Student's name is", studnetName);
print("Degree program is", degreeName);
print("Credits Left to gradaute is", creditsLeft);
