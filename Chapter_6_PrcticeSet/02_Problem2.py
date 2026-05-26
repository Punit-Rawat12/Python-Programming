marks1 = int(input("Enter Yout marks ;"))
marks2 = int(input("Enter Yout marks ;"))
marks3 = int(input("Enter Yout marks ;"))
total_percentage = (marks1 + marks2 + marks3)/300 * 10050
if(total_percentage>=40) :
    print("You are pass")
    print(f"Your total percentage was {total_percentage: .2f}%")

else:
    print("You are not pass")    
    print(f"Your total percentage was {total_percentage: .2f}%")
