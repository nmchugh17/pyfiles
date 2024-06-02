# fruits = ["Apple", "Orange", "Banana", "Mango", "Kiwi"]

# for fruit in fruits:
#     print(fruit)
#     for letter in fruit:
#         print(letter)

# print("Thats All Folks")

# for myNumber in range(1,11,1):
#     print(myNumber)

# print("Thats All Folks")

# for myNumber in range(10,-1,-1):
#     print(myNumber)

# print("Thats All Folks")

myGrades = []
numGrades = int(input("How Many Grades Do You Have? "))

for num in range(0,numGrades,1):
    grade = float(input("Please Enter Your Grade: "))
    myGrades.append(grade)

for g in myGrades:
    print(g)

print("Thats All Folks")

