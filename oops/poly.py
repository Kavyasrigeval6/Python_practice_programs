#DUCKTYPING
class A:
    def disp(self):
        print("A")
class B:
    def disp(self):
        print("B")
def call(obj):
        obj.disp()
AObj=A()
BObj=B()
call(AObj)
call(BObj)
#operator overloading
class Account:
     def __init__(self,name,bal):
          self.name=name
          self.bal=bal
     def __add__(self,other):
          return self.bal+other.bal
     def __gt__(self,other):
          return self.bal>other.bal
user1=Account("AAA",5000)
user2=Account("BBB",7000)
tot=user1+user2
print("total: ",tot)
if user1>user2:
     print("user1 has more balance")
else:
     print("user2 has more balance")
####
class A:
     def __init__(self,num):
          self.n1=num
     def __add__(self,other):
          return self.n1+other.n1
obj1=A(5)
obj2=A(8)
tot=obj1+obj2
print(tot)
#method overriding
class A:
 def disp(self):
      print("class A")
class B:
 def disp(self):
      print("class B")
obj=B()
obj.disp()#method overriding- calls disp method of class B
###
class Shape:
     def draw(self):
          print("Shape")
class Circle(Shape):
     def draw(self):
          print("Circle")
class Rectangle(Shape):
     def draw(self):
          print("Rect")
obj1=Circle()
obj2=Rectangle()
obj1.draw()
obj2.draw()
###
class Payment:
     def pay(self):
          print("Payment paid")
class CreditCard(Payment):
     def pay(self):
               print("CreditCard paid")
class UPIPayment(Payment):
     def pay(self):
               print("UPIPayment paid")
class CashPayment(Payment):
     def pay(self):
               print("CashPayment paid")
payee=Payment()
payee=CreditCard()
payee.pay()
###
class Calculator:
    def add(self,a,b,c=0):
        return a+b+c
class Calc(Calculator):
    def add(self,a,b,c=0):    
        return a+b+c
obj1=Calculator()
obj2=Calc()
print(obj1.add(5,5))
print(obj2.add(5,7,8))
print(obj2.add(5,3))



    

