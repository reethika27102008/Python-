# def Number_Analyzer():
#     def number():
#             num=input("Enter your value to add:")
#             a=0
#             for i in num:
#                 a+=int(i)
#             print(a)
#     number()


#     def number():
#             num=input("Enter your value to count:")
#             count =0
#             for i in num:
#                 count+=1
#             print(count)
#     number()

#     def reverse():
#         num = input("Enter your number to reverse: ")
#         rev = num[::-1]
#         print(rev)
#     reverse()

#     def even_odd():
#         num=int(input("Enter your value to find whether it is odd or even:"))
#         if num%2==0:
#                 print("It is a even number")
#         else:
#                 print("It is a odd number")
#     even_odd()
# Number_Analyzer()

def generate_password():
    def user_name():
        print("Generate a user name:")
        print("Convert name to lowercase")
        user=input("Enter your username: ")
        print(user.lower())
    user_name()
        
    def space():
        user=input("Enter your username: ")
        print(" Remove spaces ")
        result = user.replace(" ", "")
        print(result)
    space()

    def charcter():
        print("Take first 4 characters ")
        text = input("Enter your username: ")
        print(text[:4])
    charcter()

    def lastdigit():
        print("Add last 2 digits of ID" )
        id=(input("Enter your ID:"))
        last_two = id[-2:]      
        sum = int(last_two[0]) + int(last_two[1])
        print(sum)
    lastdigit()
generate_password()

def Uname_Pword_System():
    def password():
        print("At least 6 characters ")
        pword=input("ENTER YOUR PASSWORD:")
        if len(pword)>=6:
            print("Strong password")
        else:
            print("Sorry,weak password")
    password()

    def strong_password():
        print("Must contain uppercase, lowercase, digit, and special character ")
        password=input("Enter your password")
        for ch in password:
            if ch.isupper():
                upper = True
            elif ch.islower():
                lower = True
            elif ch.isdigit():
                digit = True
            elif not ch.isalnum():
                special = True

        if len(password) >= 8 and upper and lower and digit and special:
            print("Strong Password")
        else:
            print("Weak Password")
    strong_password()
Uname_Pword_System()