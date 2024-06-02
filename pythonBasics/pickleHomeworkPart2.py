import pickle

with open("studentData.pkl", "rb") as dataRead:
    studentData = pickle.load(dataRead)

while(1==1):
    name = input("Which Student Do You Want to Check: ")
    for i in range(0,len(studentData),1):
        if(studentData[i][0] == name):
            print(str(studentData[i][0]), "'s Grade is ", str(studentData[i][1]))