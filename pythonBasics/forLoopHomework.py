grades = []
numGrades = int(input("Enter The Number of Grades: "))
avgGrade = 0
gradesTotal = 0

for i in range(0,numGrades,1):
    grades.append(float(input("Enter the Grade: "))) 

maxGrade = grades[0]
minGrade = grades[0]

for grade in grades:
    gradesTotal += grade

    if(grade > maxGrade):
        maxGrade = grade
    
    if(grade < minGrade):
        minGrade = grade


avgGrade = sum(grades)/len(grades)
print("The Average Grade is: ", avgGrade)
print("The Highest Grade is: ", maxGrade)
print("The Lowest Grade is: ", minGrade)
print("All Grades are : ",grades)

sorted = False
while(sorted == False):
    for i in range(0,len(grades)-1,1):
        preGrade = grades[i]
        postGrade = grades[i+1]
        sorted = True
        if(preGrade < postGrade):
            grades[i] = postGrade
            grades[i+1] = preGrade
            sorted = False

print("Sorted Grades: ", grades)
