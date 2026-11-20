##student management system
'''class Student:
    def __init__(self):
        self.stud=[]
        self.nam=""
        self.max=0
    def average(self):
          for d in self.stud:
              d["tot"]=int(d["Eng"])+int(d["Mat"])+int(d["Sci"])+int(d["Soc"])
              d["avg"]=int(d["tot"])/4
    def read(self):
        with open(r"C:\Users\KAVYASRI-G6\OneDrive - G6 TECHNOLOGY SERVICES INDIA LLP\Python_practice\__pycache__\students.txt",'r') as f:
         for data in f:
            str=data.strip().split(",")
            dict={"id":str[0],"Name":str[1],"Eng":str[2],"Mat":str[3],"Sci":str[4],"Soc":str[5]}
            self.stud.append(dict)
         self.average()
    def highest(self): 
        for dic in self.stud:
            if self.max<dic["tot"]:
                self.max=dic["tot"]
                self.nam=dic["Name"]
obj=Student()
obj.read()
obj.highest()
print(f"The highest Marks is {obj.max} of {obj.nam}")
### shopping cart
class Cart:
    def __init__(self):
        self.products = {
    101: {"name": "Laptop", "price": 45000},
    102: {"name": "Mouse", "price": 500},
    103: {"name": "Keyboard", "price": 1500},
    104: {"name": "Monitor", "price": 12000},
    105: {"name": "Headphones", "price": 2500},
    106: {"name": "USB Drive", "price": 800},
    107: {"name": "Printer", "price": 8000},
    108: {"name": "Webcam", "price": 2000},
    109: {"name": "Speaker", "price": 3500},
    110: {"name": "Mobile Phone", "price": 18000}}
    def add(self,pdt):
        for id in self.products:
            for name in id:
                if name==pdt:
                  pass  
    def remove(self):
        pass
    def dec(fun):
        def wrap():
            pass
            fun()
    @dec
    def discount():
        pass


cust=Cart()
print("Menu:\nadd\nremove\ndisplaycart")
match(str):
    case "add":
        product=input("enter the product: ")
        cust.add(product)'''
########
users = [
    {"name": "Alice", "status": "inactive", "join_date": "2025-01-01"},
    {"name": "Bob", "status": "active", "join_date": "2026-05-12"},
    {"name": "Charlie", "status": "active", "join_date": "2026-11-01"},
]
list=sorted(users,key=lambda data:(data["status"],data["join_date"]))
print(list)


