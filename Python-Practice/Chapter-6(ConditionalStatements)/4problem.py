# A spam comment is defined as a text containing the following keywords : "Make a lot of money", "buy now","Subscribe this","click this".WAP to detect these spams?
p1="Make a lot of money"
p2= "buy now"
p3= "Subscribe this"
p4= "click this"

message = input("Enter your comment:")

if((p1 in message) or (p2 in message) or (p3 in message) or (p4 in message)):
    print("This comment is a Spam")
else:
    print("This comment is not spam")