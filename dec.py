import time
'''def decorator1(fun):
    def wrap():
        print("Before")
        fun()
        print("after")
    return wrap 
@decorator1
def fun1():
    print("Hi")
fun1()
#####
def dec1(fun):
    def wrap(a,b):
        if a<b:
            a,b= b,a
        fun(a,b)
    return wrap
def sub(a,b):
    print(a-b)
def div(a,b):
    print(a/b)
res1=dec1(sub)
res1(2,5)
res2=dec1(div)
res2(3,339)
#####
def perform(addl):
    def wrap(*a):
        if a[0]>5:
          addl(a)
    return wrap
@perform
def add_lst(a):
   list1.append(a)
list1=[]
nums=input("enter the elements: ").split()
print(nums)
for i in nums:
   add_lst(int(i))
print(list1)
####
def timer(fun):
    def wrap():
        start=time.perf_counter()
        res=fun()
        end=time.perf_counter()
        print("sum: ",res)
        print("Execution time: ",end-start)
        
    return wrap
@timer
def calculate():
    total = sum(range(1000000))
    return total
calculate()
#####
def uppercase(fun):
    def wrap():
        s=fun()
        return s
    return wrap
@uppercase
def get_name():
    return "python decorator"
print(get_name().upper())
####
def count_calls(fun):
    def wrap():
         global count
         count+=1
         fun()
         print(count)
    return wrap
count=0
@count_calls
def func1():
    print("hello")
func1()
func1()
func1()
###calling the function 3 times
def repeat(n):
    def dec(fun):
     def wrap():
        for i in range(n):
           fun()
     return wrap
    return dec
@repeat(3)
def greet():
    print("hello")
greet()
###add numbers
def dec1(fun):
    def wrap(a,b):
      fun(a,b)
    return wrap

@dec1
def add1(a,b):
   print(a+b)
add1(5,3)
###
def dec(fun):
   def wrap(n):
      if(n>0):
         fun(n)
      else:
         print("it is a negative number")
   return wrap
@dec
def disp(n):
   print(n)
disp(87)
disp(-988)
###
def login(fun):
     def wrap():
         str=input("enter your password")
         if(str=="abcd"):
          fun()
         else:
            print("wrong login credentials")
            print("user is logged out")
     return wrap
@login
def user():
   print("Your login credentials are correct")
 user()'''
 ###
def dec1(fun):
    def wrap(s):
        if s=="admin":
         fun()
        else:
            print("Permission is restricted")
    return wrap
@dec1
def admin():
    s=input("enter the admin password: ")
    if s=="admin01":
        print("logged in successfully")
    else:
        print("wrong credentials")
str=input("Enter admin/user: ")
admin(str)



      
        




        



    