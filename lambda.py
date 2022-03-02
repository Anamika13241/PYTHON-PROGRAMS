x=int(input("Enter the side of square:"))
area=lambda x:x*x
print("Area of square: {0}".format(area(x)))
l=int(input("Enter the length:"))
b=int(input("Enter the breadth"))
area=lambda l,b:l*b
print("The area of rectangle:{0}".format(area(l,b)))
h=int(input("Enter the height:"))
bre=int(input("Enter the breadth:"))
area=lambda h,b:0.5*bre*h
print("The area is {0}:".format(area(b,h)))

