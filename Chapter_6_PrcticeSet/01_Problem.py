no = int(input("Enter a 4 digit number"))
no1 = int(input("Enter a 4 digit number"))
no2 = int(input("Enter a 4 digit number"))
no3= int(input("Enter a 4 digit number"))
if (no > no1 and no > no2 and no > no3):
    print(no, "is greater 4 digit number")

elif (no1 > no and no1 > no2 and no1 > no3):
    print(no1, "is greater 4 digit number")

elif (no2 > no1 and no2 > no and no2 > no3):
    print(no2, "is greater 4 digit number")

else:
    print(no3, "is greater 4 digit number")
