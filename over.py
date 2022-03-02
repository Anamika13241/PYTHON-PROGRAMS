n=int(input("Enter the number of elements:"))
list=[]
p=input("Enter the values:")
for i in range(0,n):
    s=int(input())
    if s>100:
        list.append("over")
    else:
        list.append(s)
    print(list)