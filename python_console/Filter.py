import random
import csv
class location():
    def __init__(self):
        pass

    def filter(self):
        loc,opt = obj_data.filter(0,5)
        return loc,opt

class room_type(location):
    def filter(self):
        room,opt = obj_data.filter(5,10)
        return room,opt

class rent_range(room_type):       
    def filter(self):
        rent,opt = obj_data.filter(10,15)
        return rent,opt

class data_base(rent_range):
    def filter(self,start,end):
        file = open("choice.txt","r")
        preference =file.readlines()
        for i in range(start,end):
            print(preference[i])
        output = int(input("Enter your option:"))
        return preference[start+output],output
        file.close()

class operation(data_base):
    def filter(self):
        Location , option_1= obj_location.filter()
        Type,option_2 = obj_room.filter()
        Rent,option_3 = obj_rent.filter()
        print("Your preferences are : ")
        print(Location+Type+Rent)
        from Room_info import room
        obj= room()
        obj.address(option_1,option_2,option_3)
               
print("-----ENTER YOUR CHOICE-----")
obj_location=location()
obj_room=room_type()
obj_rent=rent_range()
obj_data=data_base()
obj_op=operation()
