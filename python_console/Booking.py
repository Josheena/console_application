import mysql.connector as mycon
mydb=mycon.connect(
    host="localhost",
    user="root",
    password="Aspire123",
    database="python_data"
)

def insert(name,Phno,Mailid):
    result=mydb.cursor()
    data ="insert into users (name,Phno,Mailid) values (%s,%s,%s)"
    user=(name,Phno,Mailid)
    result.execute(data,user)
    mydb.commit()
    print("Successfully inserted the Data!")


while True:
    confirm = input("Do You want to confirm Booking[yes / no]:")
    if(confirm == "yes"):
        name= input("Enter user name :")
        Phno=input("Enter phone number :")
        Mailid=input("Enter mail id :")
        insert(name,Phno,Mailid)
        break

    elif(confirm == "no"):
        print("Redirecting you to home page")
        from user_login import user_login
        user_login()

    else:
        print("Please enter the valid input")