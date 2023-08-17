
'''for i in range(1,10) :
    for j in range(1,10) :
        if i*j >= 10 :
            print(f"{j} * {i} = {i*j}",end="   ")
        else :
            print(f"{j} * {i} = {i*j}",end="    ")
    print('')'''
'''
multiply = lambda x,y : x * y
cube = lambda x : pow(x,3)
res = lambda x,y : f"{x} > {y}" if x >= y else f"{y} > {x}"
print(multiply(3,4),cube(3),res(7,7))'''
price = [("T-shirt",1890),("shoes",1790),("pant",1690)]
to_USD = lambda x : (x[0],round(x[1] / 30))
print(USDprice := list(map(to_USD,price)))
class game :
    def __init__(self,name,make,year) :
        self.name = name
        self.make = make
        self.year = year
   
ztok = game("ztok","nintendo",2023) 
a = lambda x : x - 1911
print(a(ztok.year))
