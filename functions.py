print("python")
def f1(a):
    print(a)
f1(5)
def f2(*args):
    sum=0
    for i in args:
        sum+=i
        print(sum, end=" ")
    print()
f2(1,2)
f2(2,3,4)
def f3(n):
    if(n==1):
     return 1
    else:
       return n*f3(n-1)
fact=f3(5)
print(fact)
def f4(num,**args):#saved as dictionary
    print(num)
    print(args)
f4(5,a=6,b=7)
###anonymous function###
a=lambda n:n*n
print(a(5))
even=lambda a: a%2
even(45)
if(even==0):
    print("even")
else:
    print("odd")
max1=lambda a,b,c:max(a,b,c)
print(max1(5,10,25))
result=lambda num: "positive" if(num>0) else("negative" if num<0 else "zero")
print(result(-9))
##higher order functions##
def add(num):
    return num+num
def sub(num):
    return num-num
def perform(num,fun):
    return fun(num)
nums=5
print(perform(nums,sub))
print(perform(nums,add))
######higher order using list
def add(num):
    return num+num
def sub(num):
    return num-num
def perform(num,fun):
    for i in num:
      res=fun(i)
      print(res,end=" ")
nums=[1,2,3]
perform(nums,sub)
perform(nums,add)
###higher order using lambda
def calculate(fun1,a):
    return fun1(a)
print(calculate(lambda x:x+x, 5))
result=lambda n: "positive" if n>0 else("negative" if n<0 else "zero")
a=int(input( ))
print(result(a))
price=int(input("Enter price: "))
quantity=int(input("Enter quantity: "))
tot=lambda price,quantity: price*quantity
print(tot(price,quantity))
students = [("Ravi", 85), ("Anu", 92), ("Sam", 78)]
sort_lst= lambda students: sorted(students,reverse=True)
print(sort_lst(students))
def outer():
    print("outer function")
    def inner(num):
        print("inner function")
        print(num+num)
    return inner
outer() 
a=outer()
a(5)


