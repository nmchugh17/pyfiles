import pickle

numStudents = int(input("How many Students do you have? "))
students = []

for i in range(0,numStudents,1):
    studentName = input("Enter the Student Name: ")
    studentGrade = float(input("Enter the Student Grade: "))
    students.append([studentName,studentGrade])

with open("studentData.pkl", "wb") as s:
    pickle.dump(students,s)

with open("studentData.pkl", "rb") as s1:
    studentList = pickle.load(s1)

for s in studentList:
    print("The Student Name is ", s[0])
    print("The Student Grade is ", s[1])

