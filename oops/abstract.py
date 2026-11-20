from abc import ABC,abstractmethod
class abs(ABC):
    def disp(self,n):
        print(n)
obj=abs()
obj.disp(10)
####
class Payment(ABC):#abstractclass
    @abstractmethod
    def pay(self):
        pass
class A(Payment):
    def pay(self):
        print("A-pay")
class B(Payment):
    def pay(self):
        print("B-pay")
class Purchase:
    def __init__(self,gateway):
        self.gateway=gateway
    def checkout(Self): 
        print("checking out")
        Self.gateway.pay()
gateway1=A()
gateway2=B()
pur1=Purchase(gateway1)
pur2=Purchase(gateway2)
pur1.checkout()
pur2.checkout()
#####
from abc import ABC,abstractmethod
class Appliance(ABC):
    @abstractmethod
    def turnOn(self):
        pass
class Fan(Appliance):
    def turnOn(self):
           print("Fan is turned on")
class Fridge(Appliance):
    def turnOn(self):
            print("Fridge is turned on")
class A:
     def __init__(self,device):
         self.device=device
     def func(self):
          self.device.turnOn()
          
fan1=Fan()
frdge=Fridge()
app1=A(fan1)
app2=A(frdge)
app1.func()
app2.func()
##
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
class Circle(Shape):
    def __init__(self,rad):
        self.rad=rad
    def area(self):
        print("Area of circle: ", 3.14*self.rad**2)
class Rectangle(Shape):
    def __init__(self,len,bred):
        self.len=len
        self.bred=bred
    def area(self):
        print("Area of Rectangle: ",self.len * self.bred)
class perform:
    def __init__(self,obj):
        self.obj=obj
    def call(self):
        self.obj.area()
cobj=Circle(42)
robj=Rectangle(25,14)
obj1=perform(robj)
obj2=perform(cobj)
obj1.call()
obj2.call()
###
class Employee(ABC):
    @abstractmethod
    def calculate_salary(self):
        pass
class Fulltime(Employee):
    def __init__(self,hours):
         self.base=5000
         self.hours=hours
    def calculate_salary(self):
        print(f"fulltime salary for {self.hours} hours:",self.base * self.hours)
class Partime(Employee):
    def __init__(self,hours):
             self.base=2000
             self.hours=hours
    def calculate_salary(self):
            print(f"parttime salary for {self.hours} hours:",self.base * self.hours)
class A:
     def __init__(self,obj):
          self.obj=obj
     def calculate(self):
          self.obj.calculate_salary()
f=Fulltime(8)
p=Partime(3)
obj1=A(f)
obj2=A(p)
obj1.calculate()
obj2.calculate()
###
class Notification(ABC):
     @abstractmethod
     def send(self):
          pass
class Email(Notification):
     def send(self):
          print("Email Notification is sent")
class SMS(Notification):
     def send(self):
          print("SMS Notification is sent")
def call(obj:Notification):
          obj.send()
en=Email()
sn=SMS()
call(en)
###


     





