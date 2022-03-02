class rectangle:
    def __init__(self,l,b):
        self.len=l
        self.br=b
    def area(self):
        area1=self.len*self.br
        return area1
    def perimeter(self):
        perimeter1=2*(self.len+self.br)
        print(perimeter1)
    def comp(self,obj):
        if(self.area()>obj.area()):
            print("GREATER")
        else:
            print("LESSER")
rect1=rectangle(10,20)
rect1.perimeter()
obj=rectangle(30,40)
obj.perimeter()
rect1.comp(obj)