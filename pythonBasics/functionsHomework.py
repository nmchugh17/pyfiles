def inputGrades(nm):
    grades = []
    for i in range(0,nm,1):
        grd = float(input("Please Enter your Grade: "))
        grades.append(grd)
    return grades

def printGrades(nm,x):
    for i in range(0,nm,1):
        print(x[i])

def averageGrades(nm,x):
    tot=0
    for i in range(0,nm,1):
        tot+=x[i]

    average = tot/nm
    return average

def highLow(nm,x):
    highG = 0
    lowG = 100
    for i in range(0,nm,1):
        if (x[i]<lowG):
            lowG=x[i]
        if (x[i]>highG):
            highG=x[i]
    
    return highG, lowG
        

    
    return average

numGrades=int(input("How many grades? "))
myGrades = inputGrades(numGrades) 
print(" ")
print("Your Grades Are: ")
printGrades(numGrades,myGrades)
avg = averageGrades(numGrades, myGrades)
print("Your Average is: ", round(avg,1))
highG, lowG = highLow(numGrades, myGrades)
print("Your High Grade is: ", highG)
print("Your Low Grade is: ", lowG)