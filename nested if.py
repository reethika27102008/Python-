# Task 1
db_email="reethika2008@gmail.com"
db_password="reethi@2008"
email=(input("Enter your email:"))
password=(input("Enter your password:"))
if email!="" and password!="":
    if email==db_email:
        if password==db_password:
            print("Login successful")
        else:
            print("invalid Password")
    else:
        print("Invalid email")
else:
    print("Login unsuccessful")
# Task2

        
    