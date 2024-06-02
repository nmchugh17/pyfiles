class Student:

    def __init__(self, firstName, lastName):
        self.firstName = firstName
        self.lastName = lastName

    def studentGrades(self,numG):
        self.grades = []
        for i in range(0,numG,1):
            grade = float(input("Enter the Students Grades: "))
            self.grades.append(grade)
        return self.grades
    
    def averageHighLowGrages(self):
        self.avg = 0
        self.high = 0
        self.low = 100
        total = 0

        for g in self.grades:
            total += g

            if(g > self.high):
                self.high = g
            if(g < self.low):
                self.low = g

        self.avg = total/len(self.grades)

        return self.avg, self.high, self.low
    
    def printStudentDetails(self):
        print("The Student Name is", self.firstName, self.lastName)
        print("The Student Grades are: ")
        for g in self.grades:
            print(g)
        print("The Student Average Grade is: ", self.avg)
        print("The Student Highest Grade is: ", self.high)
        print("The Student Lowest Grade is: ", self.low)

firstName = input("Please Enter the Students First Name: ")
lastName = input("Please Enter the Students Last Name: ")

student1 = Student(firstName,lastName)
numGrades = int(input("Please Enter the Number of Grades for the Student: "))
student1.studentGrades(numGrades)
student1.averageHighLowGrages()
student1.printStudentDetails()




            
