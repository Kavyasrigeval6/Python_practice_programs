from threading import Thread
from time import *
'''class A(Thread):
    def run(self):
        for i in range(5):
            print("Hi",i+1)
            sleep(0.2)
class B(Thread):
    def run(self):
        for i in range(5):
             print("Hello",i+1)
             sleep(0.3)
t1=A()
t2=B()
t1.start()
t2.start()
####
def disp():
    for i in range(3):
       print(i+1,"hello")
       sleep(0.2)
def show():
    for i in range(3):
       print(i+1,"hi")
       sleep(0.3)

t1=Thread(target=disp)
t2=Thread(target=show)
t1.start()
t2.start()
t1.join()
t2.join()
print("end of thread execution")'''
#### 
def download(file_name):
    print("Downloading file... ",file_name)
    sleep(0.5)
    print("Download Complete",file_name)

files=['img1.jpg','img2.jpg','img3.jpg']
threads=[]
for f in files:
    t=Thread(target=download,args=(f,))
    threads.append(t)
start=time()
for t in threads:
    t.start()
for t in threads:
    t.join()
end=time()
print(f"time to complete: {end-start:.2f} secs")
