from abc import ABC
class Hotel(ABC):
    name=[]
    avail=[]
    loc=[]
class Price(Hotel):
   price=[]
   rating=[]
   @classmethod
   def getdetails(cls):
        with open("C:\\Users\\KAVYASRI-G6\\OneDrive - G6 TECHNOLOGY SERVICES INDIA LLP\\Python_practice\\__pycache__\\hotel","r") as file:
            for line in file:
                data=line.split()
                cls.name.append(data[0])
                cls.avail.append(int(data[1]))
                cls.loc.append(data[2]) 
                cls.rating.append(int(data[3]))
                cls.price.append(float(data[4]))
class User:
    def __init__(self,Id,name,hotel,room,cost):
       self.Id=Id
       self.name=name
       self.hotel=hotel
       self.room=int(room)
       self.cost=float(cost)
Price.getdetails()
obj=Price() 
#########
userId=1
userlist={}
def useradd():
 global userId
 username=input("Enter the name: ")
 if not username:
    raise ValueError("Invalid UserName")
 with open("C:\\Users\\KAVYASRI-G6\\OneDrive - G6 TECHNOLOGY SERVICES INDIA LLP\\Python_practice\\__pycache__\\hotel","r") as file:
   for line in file:
     print(line)
 userhotel=input("Which hotel do you prefer: ")
 if not userhotel or userhotel not in Hotel.name:
    print("Invalid hotel name")
    return
 index=Hotel.name.index(userhotel)
 userroom=int(input("Enter the no of rooms:"))
 if not userroom:
    print("Invalid value")
    return
 if userroom > Hotel.avail[index]:
    print(f"Required rooms are not available. availability: {Hotel.avail[index]}")
    return
 usercost=userroom*Price.price[index]

 user=User(userId,username,userhotel,userroom,usercost)
 userlist[userId]=user
 Hotel.avail[index]-=userroom
 with open("userlist","a") as file:
   file.write(f"{userId} {username} {userhotel} {userroom} {usercost}\n")
 print(f"Room booked Successfully with UserId {userId}")
 userId+=1
 keepuser()
########
def remove():
   userRId=int(input("Enter User Id: "))
   if not userRId:
       raise ValueError("Invalid User Id")
   if userRId not in userlist:
      print("Not a user")
      return
   user=userlist[userRId]
   index=Hotel.name.index(user.hotel)
   str=input("Let us know You want to checkout(Yes/No)").lower()
   if str=='yes':
    Hotel.avail[index]+=user.room
    userlist.pop(userRId)
    print("You successfully Checked out")
    keepuser()
########
def view():
   totcost=0
   uservId=int(input("Enter the userId:"))
   if not uservId:
          raise ValueError("Invalid User Id")
   if uservId not in userlist:
         print("Not a user")
         return
   user=userlist[uservId]
   totcost=user.cost+user.cost*0.05
   print(f"UserId:{user.Id}\nUserName:{user.name}\nHotel Booked:{user.hotel}\nNo of Rooms:{user.room}\nTotal Bill(incl 5%GST):{totcost}")
##########
def keepuser():
   global userId
   #print(userId)
   with open("userlist","a+") as file:
      file.seek(0)
      for line in file:
         data= line.split()
         Id=int(data[0])
         name=data[1]
         hotel=data[2]
         room=data[3]
         cost=data[4]
         user=User(Id,name,hotel,room,cost) 
         userlist[Id]=user
         userId=max(userId,Id+1)
###########  
f=open("userlist")
while True: 
 print("******Hotel Booking APP******")    
 print("Available services: 1.Check-In\n2.Check-out\n3.view Bill\n4.Exit")
 n=int(input()) 
 match(n):
   case 1:
     try: 
      useradd()
     except ValueError as e:
        print(e)
   case 2:
      try:
       remove()
      except ValueError as e:
         print(e)
   case 3:
       try:
        view()
       except ValueError as e:
        print(e)
   case 4:
       print("Thanks for choosing us!!")
       break
   case _:
    print("Invalid choice")


