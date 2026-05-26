p1 = "Makes a lot of money " 
p2 = "Buy this " 
p3 = "Subscribe"
p4 = "Click this"
message = input("Enter your comment :")
if(p1 in  message or p2 in  message or  p3 in  message or p4 in  message  ) :
    print("This comment is a spam")
else:
    print("This comment is not a spam ")
        