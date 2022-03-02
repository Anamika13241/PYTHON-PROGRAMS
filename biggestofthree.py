a=int(input("Enter 1st no "))
b=int(input("Enter 2nd no "))
c=int(input("Enter 3rd no "))
if a>b and a>c:
    print("Greatest number is ",+str(a))
elif b>a and b>c:
    print("Greatest number is ",+str(b))
else:
    print("Greatest number is "+str(c))