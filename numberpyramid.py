a=int(input("Enter a number:"))
for i in range(1,a+1):
    for j in range(1,i+1):
        print(i*j,end=" ")
    print("\n")

x=int(input("Enter a side:"))
area=lambda x:x*x
print("The area is {0}:".format(area(x)))
l=int(input("Enter the length:"))
b=int(input("Enter the breadth:"))
area=lambda l,b:l*b
print("The area is {0}:".format(area(l,b)))

b=int(input("Enter a number:"))
for i in range(1,b+1):
    if b%i==0:
        print(i)

k=int(input("Enter the limit:"))
a=0
b=1
c=a+b
print(a)
print(b)
print(c)
for i in range(2,k):
    d=b+c
    print(d)
    b=c
    c=d

set1={"red","pink","blue"}
set2={"blue","pink","green"}
set3=set1.difference(set2)
print(set3)

d=input("Enter the filename:")
a=d.split(".")
print(a)
print("The extension is "+a[-1])


