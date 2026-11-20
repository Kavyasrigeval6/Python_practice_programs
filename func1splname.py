'''import module1
s=module1.add()
print(s)
####
from module1 import  add
s=add()
print(s)
from module1 import *
s1=add()
s2=sub()
print(s1,s2)'''
print(globals())
print(__name__)
