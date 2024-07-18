a=[1,"ali",1.54]
a[2]
b=[1,"ali",1.54]
b.append(1000)
b
b.pop()

g={"1010":{"name":"tehran","pop":15},
   "1011":{"name":"yazd","pop":1}}
g["1010"]

f={"a":1000,"b":400}
for i , t in f.items():
    print (i,">----",t)

y={10,13,13,13,12}
z={10,14,13}
y.union(z)
y.difference(z)
y.issubset(z)

os.getcwd()


def zoj (l:list)-> list:
    u=[]
    for i in l:
        if i % 2==0:
            u.append(i)
        return u
    print(zoj([1,5,4,2,5,7,8,9]))



    class mostatil:
        def __init__(self,a,b) :
            self.toll=a
            self.arz=b
              
        def area(self):
            return self.toll*self.arz
        
