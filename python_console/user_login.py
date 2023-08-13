import re
import csv
class user_login():
    def __init__(self):
        pass

    def register(self):
        print("\n*****Register here*****\n")
        name,password = obj_1.details()
        condition = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{8,16}$"
        match = re.compile(condition)
        if (bool(re.search(match, password))==True):
            c_password = input("Confirm password : ")
            if (password==c_password):
                l=[]
                l.append(name)
                l.append(password)
                with open('Data.csv','a',newline="") as f:
                    d =csv.writer(f)
                    d.writerow(l)
                
                print("\n-------Registered Successfully--------")
                obj_1.login()
                
            else:
                print("\nPlease enter the correct password")
        else:
                print("\nPassword should contails Capital letter,digits and spacial cases") 
                obj_1.register()
            
    def login(self):
            print("\n*****Enter Login details*****\n")
            login_name,login_password = obj_1.details()
            Flag = 0
            with open('Data.csv','r') as f:
                d=csv.reader(f)
                for x in d: 
                    if(x[0]==login_name and x[1]==login_password):
                        print("\n*****Successfully logged in*****")
                        print("\nWelcome",login_name,"!")
                        Flag = 1 
                        from Filter import operation
                        obj_op= operation()
                        obj_op.filter()
                        
            if(Flag==0):
                print("Invalid login")
                obj_1.login()

class user_details(user_login):
    def details(self):
        name=input("Enter your name : ")
        upassword=input("Enter password :" ) 
        return name,upassword

print(" ***** Welcome to XYZ Tenant Finder Services *****")
print(" \t 1. Register\n ")
print(" \t 2. Login\n")
user_option = int(input("Enter your option: "))
obj_1 = user_details()
if user_option == 1:
    obj_1.register() 
elif user_option == 2:
    obj_1.login()
else:
    print("please enter the valid option")