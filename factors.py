def factor(n):
    print("The factors of "+str(n)+" are ")
    for i in range(1,n+1,1):
        if n%i==0:
            print(i)
factor(int(input("Enter a number")))

