from functools import reduce
list1=[10,55,32,75,90,41,68]
list2=list(filter(lambda n: n>50,list1))
print(list2)
nums=[2,9,8,6,76,0,53,45]
list1=list(filter(lambda n:n%2==0,nums))
print(list1)
nums1=[2,4,8,10]
doubled=list(map(lambda n:n*2,nums1))
print(doubled)
nums1=[2,4,8,10]
sum=reduce(lambda a,b:a+b,nums1)
print(sum)
list1=[2,3,4]
cube=list(map(lambda n:n**3,list1))
res=reduce(lambda a,b:a+b,cube)
print(res)
list1=[2,3,4]
print(reduce(lambda a,b:a*b,map(lambda n:n**2,list1)))
names = ["ravi", "anu", "sam"]
list1=list(map(lambda s:s.upper(),names))
print(list1)
num=[-5,3,-2,0,7,-9]
list1=list(filter(lambda n: n<0,num))
print(list1)
name=["Ravi", "Priya", "Alexander", "Sam"]
list2=list(filter(lambda s:len(s)>4,name))
print(list2)
temp=[0, 20, 30, 100]
fahnt=list(map(lambda n: n*9/5 +32,temp))
print(fahnt)
list3=list(map(lambda n:str(n),num))
print(list3)
print(reduce(lambda a,b:max(a,b),num))
value=[1,2,3,4,5]
filter1=list(filter(lambda n:n>3,value))
print(reduce(lambda a,b:a+b,map(lambda n:n**3, filter1)))