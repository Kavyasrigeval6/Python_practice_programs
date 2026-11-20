'''users = [
    {"name": "Alice", "status": "inactive", "join_date": "2025-01-01"},
    {"name": "Bob", "status": "active", "join_date": "2026-05-12"},
    {"name": "Charlie", "status": "active", "join_date": "2026-11-01"},
]
list1=sorted(users,key=lambda data:data["join_date"],reverse=True)
list2=sorted(users,key=lambda data:data["status"])

print(list2)
############
class InsuficientFundsError(Exception):
    def __init__(self,amnt,balance):
        self.amnt=amnt
        self.balance=balance
try: 
  raise InsuficientFundsError(5000,1200) 
except InsuficientFundsError:
   print("Transaction Denied: Requested ₹5000 but balance is only ₹1200.")
###########
class InsuficientFundsError(Exception):
    def __init__(self,name):
        self.name=name
    def __str__(self):
        return "Invalid name"
try:
    raise InsuficientFundsError("90Abc")
except InsuficientFundsError as e:
    print(e)#callls e.__str__()
##########
from time import time,sleep
from functools import wraps

def time_it(fun):
    @wraps(fun)
    def inner():
        start=time()
        fun()
        end=time()
        print(end-start)
    return inner
@time_it
def disp():
    print("How are you?")
    sleep(0.5)
disp()
#########
str="ABCD"
s=str.lower()
print(str.lower())
print(str)'''
#########guessing random number game#######
import random
def guess(num):
   n=int(input("Guess a Number= "))
   if num == n:
    print("yes that's the number")
   else:
     raise ValueError("Wrong Try again")
   if attempt== 1:
            print("Sorry better luck next time!")
attempt=5
print("Guess a Number(5 attempts)")
n=random.randint(1,5)
while attempt>0:
 try:
  guess(n)
  break
 except ValueError as ve:
    print(ve)
 attempt-=1 



        
