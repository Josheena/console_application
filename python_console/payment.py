import re
import csv

class InvalidData(Exception):
    pass

class payment():
    def payment_mode(self):
        print("-----MAKE PAYMENT-----")
        mode=["1.Debit card","2.Credit card","3.UPI "]
        for item in mode:
            print(item)
        user_mode=int(input("Enter your mode of payment:"))
        if (user_mode==1):
            obj_5.card("Debit")
        elif (user_mode==2):
            obj_5.card("Credit")
        elif(user_mode==3):
            obj_5.upi()
        else:
            print("invalid input")
            obj_5.payment_mode()
        
    def card(self,card):
        print("Enter your",card,"card Details:")
        card_number = input("Enter card number:")
        if(len(card_number)==16):
            Holder = str(input("Enter card holder name:"))
            if (bool(re.findall('[A-Za-z]',Holder))==True):
                Rent= obj_5.price_amount()
                print("Rent:",Rent)
                obj_5.confirm_pay(Rent)
            else:
                print("Enter the valid card holder name")
                obj_5.card(card)
        else:
            print("Invalid card number")
            obj_5.card(card)
            
    def upi(self):
        print("You have chosen UPI method")
        upi_id=input("Enter UPI ID :")
        obj_5.upi_condition(upi_id)
        
    def confirm_pay(self,amount):
        print("*****Confirm Payment*****")
        choice=input("Enter yes / no to confirm payment:")
        if (choice == "yes"):
            obj_5.pin_verification()
            print("Payment done successfully")
            print("Booking done successfully !")
            print("------Thank you------")
            obj_5.redirection()
                 
        elif(choice == "no"):
            print("Redirecting to Login Page")
            obj_5.redirection()
    def upi_condition(self,id):
        condition = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{8,10}$"
        match = re.compile(condition)
        if (bool(re.search(match,id))==True):
            Rent= obj_5.price_amount()
            print("Rent:",Rent)
            obj_5.confirm_pay(Rent)
        else:
            print("Invalid UPI Id")
            obj_5.upi()

    def price_amount(self):
        with open('Option.csv','r') as f:
            d=csv.reader(f)
            for x in d:
                return x 
            
    def pin_verification(self):
        pin=input("Enter your 4 digit pin:")
        try:
            if len(pin)<4 or len(pin)>4:
                raise InvalidData
        except InvalidData:
            print("Pin number should be 4 digits\nPlease provide valid pin number")
            print("------Please try again-------")
            obj_5.payment_mode() 

    def redirection(self):
        from user_login import user_login
        obj= user_login()
        obj.login()

obj_5= payment()
obj_5.payment_mode()