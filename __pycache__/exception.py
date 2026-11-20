'''try:
    a=int(input("Enter numerator: "))
    b=int(input("Enter denominator: "))
    result=a/b
    print("Result: ",result)
except ZeroDivisionError as zde:
    print(zde)
except ValueError as ve:
    print("Check the input",ve)
finally:
   print("end of execution")
#####2
list1=[1,2,3,4,5]
try:
    ind=int(input("Enter the index: "))
    print(f"The element at position {ind} is", list1[ind])
except IndexError as ie:
    print(ie,":Invalid Index entered")
except ValueError as ve:
    print(ve,":Invalid type of Index")
finally:
    print("Execution Ended")
 #####3
dict={"Amit":50000,"Bala":85000,"Iniya":75000}
try:
    i=input("Enter the employee name: ")
    print(f"salary of the employee {i} is: ",dict[i])
except KeyError:
    print(f"Employee {i} doesn't exist")
print("logged out")
#####4
try: 
    file1=input("Enter the file to open: ")
    with open(file1,'r') as file:
        content=file.read()
        print(content)
except FileNotFoundError as fe:
     print(fe)
finally:
    print("Operation Completed")
#####5
try:
    age=int(input("Enter the age: "))
    if age<0:
      raise ValueError("Age cannot be negative")
    elif age>120:
      raise ValueError("Age cannot be greater than 120")
    else:
        print("valid age")
except ValueError as e:
       print("Error: ",e)'''
###6banking sytem using exceptions
class InsufficientError(Exception):
    pass
class BankAccount:
    def __init__(self,balance): 
        self.balance=balance
    def withdraw(self,amount):
        if amount<=0:
            raise ValueError("Invalid amount value")
        if amount>self.balance:
            raise InsufficientError("Insufficient balance")
        self.balance-=amount
        print("withdrawl successful")
        print("Remaining balance:", self.balance)
    def deposit(self,depamnt):
        if depamnt<=0:
            raise ValueError("Invalid amount value")
        self.balance+=depamnt
        print("Amount deposited successfully")
        print("Remaining balance:", self.balance)
    def disp(self):
        print(self.balance)

account= BankAccount(20000)
while True:
 print("Welcome to Banking System:")
 print("Services: 1.Withdraw\n2.Deposit\n3.Display the Balance")
 n=int(input())
 match(n):
    case 1:
       try:
        amount=float(input("Enter withdrawl amount: "))
        account.withdraw(amount)
       except ValueError as ve:
             print(ve,":Transaction failed")
       except InsufficientError as ie:
            print(ie,":Transaction failed")
       break
    case 2:
           try:
            amount=float(input("Enter the depositing amount: "))
            account.deposit(amount)
           except ValueError as ve:
                 print(ve,":Transaction failed")
           break
    case 3:
            account.disp()
            break

print("Thankyou!!")
        

