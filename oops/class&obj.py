class A:
    s='classA'#class variable
    def __init__(self):
        print("init")
    def fun1(self):
        print("class")
    def fun2(self,x):
        print(x)
obj1=A()
obj2=A()
A.fun1(obj1)# calling fun method1
obj1.fun1()# calling fun method2
obj1.var1=5 #creating variable using obj
print(obj2.s)
obj2.fun2(5)
class B:
    num=50#class variable
    def __init__(self, n,str):
        self.n=n#instance variable
        self.s=str
        def fun():
            print(self.n)
            print(self.s)
        fun()

obj1=B(100,'AAA')
print(obj1.num)
print(B.num)
##constructor
class A:
    def __new__(cls):
        print ("construtor")
        return super(A,cls).__new__(cls)
    def __init__(self):
        print("initializer")
    def disp(self):
        print("Display")

obj1=A()#calls constructor and initializer
obj1.disp()

obj2=A.__new__(A)#calls constructor
obj2.__init__()#calls initializer
obj2.disp()
obj3=A()#calls constructor and initializer
###
class A:
    num=10
    def __init__(self,n,str):
        print("init has called")
        self.n=n
        self.str=str
        print(n,str)
    @classmethod
    def info(cls):
        obj2=cls(200,'BBB')
        return obj2.num
    @staticmethod 
    def check(x):
        print(x)
obj1=A(100,'AAA')
print(A.info())# class itself goes as an arguement
A.check(50)
class A:
    num=50
    def __init__(self,name):
        self.name=name
    @staticmethod
    def disp(student):
       print(student.name)
    def disp1():
       print(A.num)
stud=A("AAA")
A.disp(stud)
A.disp1()
###
class Student:
    @classmethod
    def display(cls):#cls=A-- here it takes A itself as arguement
        print(cls)

Student.display()



