grades = []
i = 0
j=0
numGrades = int(input("Enter the Number of Grades: "))

while(i < numGrades):
    grades.append(float(input("Input the Grade: ")))
    i+=1

while(j < len(grades)):
    print(grades[j])
    j+=1 