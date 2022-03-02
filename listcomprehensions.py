list=[1,2,3,4,-9,-8,-7,-6]
n=[i for i in list if i>0]
print(n)

s=int(input("Enter the range"))
sq=[x**2 for x in range(1,s+1)]
print(sq)

v=input("Enter a word:")
vow=[m for m in v if m=='a'or m=='A'or m=='e'or m=='E'or m=='i'or m=='I'or m=='o'or m=='O'or m=='u'or m=='U']
print(vow)

w=input("Enter a word:")
d=[ord(i) for i in w]
print(d)