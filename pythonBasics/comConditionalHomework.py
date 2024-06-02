myNumber = float(input("Please Input Your Number: "))

if(myNumber == 0):
    print("Your Number is ZERO")
elif(myNumber > 0 and myNumber % 2 == 0):
    print("Your Number is POSITIVE and EVEN")
elif(myNumber < 0 and myNumber % 2 == 0):
    print("Your Number is NEGATIVE and EVEN")
elif(myNumber > 0 and myNumber % 2 > 0):
    print("Your Number is POSITIVE and ODD")
elif(myNumber < 0 and myNumber % 2 > 0):
    print("Your Number is NEGATIVE and ODD")