import random
import csv
class room():
    
    def __init__(self):
        self

    def address(self,option_1,option_2,option_3):
        for i in range(1,5):
            if(option_1 == i):
                if(option_2 == 1) and (option_3==1):
                    obj_3.details(0,2,option_1)
                    price=random.choice(range(7000,10000,500))
                    print("Rent Amount: ",price)  
                elif(option_2 == 1) and (option_3==2):
                    obj_3.details(2,4,option_1)    
                    price=random.choice(range(11000,15000,500))               
                    print("Rent Amount: ",price)  
                elif(option_2 == 2) and (option_3==2):
                    obj_3.details(4,6,option_1)
                    price=random.choice(range(11000,15000,500))               
                    print("Rent Amount: ",price)  
                elif(option_2 == 2) and (option_3==3):
                    obj_3.details(6,8,option_1)
                    price=random.choice(range(16000,20000,500))               
                    print("Rent Amount: ",price)                    
                elif(option_2 == 3) and (option_3==3):
                    obj_3.details(8,10,option_1)
                    price=random.choice(range(16000,20000,500))               
                    print("Rent Amount: ",price)                    
                elif(option_2 == 3) and (option_3==4):
                    obj_3.details(10,12,option_1)
                    price=random.choice(range(21000,25000,500))               
                    print("Rent Amount: ",price)                    
                elif(option_2 == 4) and (option_3==4):
                    obj_3.details(12,14,option_1)    
                    price=random.choice(range(21000,25000,500))               
                    print("Rent Amount: ",price)             
                else:
                    print("Invalid Search---Search not Found")
                    from user_login import user_login
                    obj= user_login()
                    obj.login()
            else:
                continue

        amount=[]
        amount.append(price)
        with open('Option.csv','a',newline="") as f:
            d =csv.writer(f)
            d.writerow(amount)
        with open('Option.csv','r') as f:
            d=csv.reader(f)
            print("amount: ",amount)
        
    def details(self,start,end,option):
        print("Address:")
        file = open("address.txt","r")
        det =file.readlines()
        for i in range(start,end):
            print(det[i])
        file.close()
        obj_3.location(option)

    def location(self,option):
        Chennai=["Thambaram - 600045","Siruseri - 603103","Padur - 600021","Adayar - 600020","Guindy - 600032"]
        Bangalore=["Koramangalam - 560034","Yeshwantpur - 560022","Electronic city - 560100","Whitefield - 560066"]
        Mumbai = ["Malad - 400064","Bandra - 400050","Orlem - 400064","bandarwada - 431506"]
        Delhi = ["Uttam Nagar - 110059","Laxmi Nagar - 110092","Khanpur - 110009"]
        if(option==1):
            print("Location:",random.choice(Chennai))
            print("City: Chennai")
        elif(option==2):
            print("Location:",random.choice(Bangalore))
            print("City: Bangalore")
        elif(option==3):
            print("Location:",random.choice(Mumbai))
            print("City: Mumbai")
        else:
            print("Location:",random.choice(Delhi))
            print("City: Delhi")
        print("Contact_info:","+91",random.choice(range(9745639860,9942351230)))
        print("Flat Available from:",random.choice(range(0,30)),"-",random.choice(range(1,13)),"-","2023")
        
obj_3=room()
