def longest(a):
    max=len(a[0])
    temp=a[0]
    for i in a:
        if(len(i)>max):
            max=len(i)
            temp=i
    print("the longest word is "+temp+" and the length of it is "+str(max))
a=["ammu","anamika","kannolii"]
longest(a)