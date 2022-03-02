x=int(input("Enter the current year"))
y=int(input("Enter the final year"))
for n in range(x,y):
    if n%4==0 and n%100!=0 or n%400==0:
        print(n)

