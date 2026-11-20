'''class A:
    def f1(self):
        print("FUNCTION1")
    def f2(self):
        print("FUNCTION2")
class B(A):
    def f3(self):
        print("FUNCTION3")
    def f4(self):
        print("FUNCTION4")
    def show(self):
        print("BSHOW")
class C(B):
    def f5(self):
        print("FUNCTION5")
obj1=B()
obj2=C()
obj1.f1()
obj1.f3()
obj2.f1()
obj2.f4()
obj2.f5()
#####
class A:
    def show(self):
      print("Class A")
class B:
    def show(self):
      print("Class B")
class C(A,B):
   def disp(self):
      print("Class C")
obj1=C()
obj1.show()
B.show(obj1)
#####
class A:
    def show(self):
      print("Class A")
class B():
    def show(self):
      print("Class B")
class C(A):
   def disp(self):
      print("Class C")
class D(B,C):
   def disp(self):
         print("Class D")
   
obj1=C()
obj1.show()
B.show(obj1)
obj2=D()
obj2.show()#prints only Class B
####
class A:
    def __init__(self):
        print("initA")
    def f1(self):
            print("FUNCTION1")
class B(A):
     def __init__(self):
          super().__init__()#calls base class init
          print("initB")
     def f2(self):
          super().f1()#calls f1function
          print("FUNCTION2")
obj1=B()
obj1.f2()
class Person:
    def __init__(self,name):
        self.name=name
    def disp(self):
          print(self.name)
class Employee(Person):
    def __init__(self,empid):
            super().__init__("AAA")
            self.empid=empid
    def disp(self):
              super().disp()
              print(self.empid)
class Manager(Employee):
     def __init__(self,dep):
                 super().__init__("101")
                 self.dep=dep
     def disp(self):
              super().disp()
              print(self.dep)
emp=Manager("AI")
emp.disp()
###
class Student:
    def __init__(self,Emark, Mmark, Smark):
        self._Emark=Emark
        self._Mmark=Mmark
        self._Smark=Smark

class Result(Student):
    def __init__(self,Emark, Mmark, Smark):
        super().__init__(Emark, Mmark, Smark)
    def disp(self):
            if self.tot>280:
                print("A grade")
            elif 260<self.tot<=280:
                print("B grade")
            elif 200<self.tot<=260:
                print("C grade")
            else:
                print("D grade")
    
    def calculate(self):
        self.tot= self._Emark+ self._Mmark+ self._Smark
        self.disp()
    
stud1=Result(98,75,86)
stud1.calculate()
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
####
class A:
    def __init__(self):
        print("class A")
class B(A):
    def __init__(self):
        super().__init__()
        print("class B")
class C(B):
    def __init__(self):
        super().__init__()
        print("class C")

objc=C()'''
###
class Vehicle:
    def __init__(self,brand):
        self.brand=brand
class Car(Vehicle):
    def __init__(self,model):
        self.model=model
        super().__init__("Tata")
    def disp(self):
        print("brand: ",self.brand)
        print("model: ",self.model)
car1=Car("nexon")
car1.disp()
###



        









    

