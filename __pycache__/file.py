f=open("data",'w')
f.write("Hi this is Python")
f=open("data",'a')
f.write(",coding language")
f=open("data",'r')
print(f.read())
f=open("data",'a')
f1=open("abc",'w')
f1.write("Python supports multiple programming paradigms—including procedural, object-oriented, and functional programming—and features " \
"a vast batteries-included standard library alongside a rich ecosystem of third-party packages." \
"Because of its versatility and ease of use, it is widely applied in artificial intelligence, machine learning, data analysis, web development, and task automation")
f1=open("abc",'r')
for data in f1:
   f.write(data)
f1.close
f.close
f2=open("newfile",'x')
#####
f=open("data",'r')
count=0
for data in f:
   count+=1
print(count)
#### count words in file
f=open("data",'r')
count=0
for data in f.read().split():
   count+=1
print("No of words: ",count)
#### count chars in file
f=open("data",'r')
count=0
for data in f.read().split():  
   count+=len(data)+1
print("No of chars: ",count)
###count vowels in file
f=open("data",'r')
count=0
for data in f.read().split():  
   for ch in data:
      if ch.lower() in "aeiou":
         count+=1
print("No of vowels: ",count)
###count uppercase in file
f=open("data",'r')
count=0
for data in f.read().split():
   for ch in data:
      if ch.isupper():
        count+=1
print("No of uppercase: ",count)
###count "Python" in file
f=open("data",'r')
count=0
for data in f.read().split():
    if data=="Python":
        count+=1
print("No of 'Python' : ",count)
###copying even number lines from data to abc file
f=open("abc",'r')
f1=open("newfile",'w')
count=0
for data in f:
    count+=1
    if count%2==0:
      f1.write(data)
###print words in reverse order
f1=open("newfile",'r')
for data in f1:
    for str in data.split():
        print(str[::-1],end=" ")
###find longest word in file
f=open("names",'w')
f.write("Abi\nBala\nDeepa\nKaran\nRiya")
f=open("names",'r')
max=0
for data in f:
    if max<=len(data):
        max=len(data)
        str=data
print(str)


