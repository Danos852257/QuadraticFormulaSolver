import math
def solver(a, b, c):
    discriminant = (b*b)-(4*a*c)
    if discriminant == 0:
        return (str((-1*b)/(2*a)))
    if discriminant<0:
        discriminant*=-1
        if int(math.sqrt(discriminant)) == math.sqrt(discriminant):
            discriminant = math.sqrt(discriminant)
            pos = (str((-1*b)/(2*a))+"+"+(str(discriminant)+"i/"+str(2*a)))
            neg = (((str((-1*b)/(2*a)))+"-"+(str(discriminant)+"i/"+str(2*a))))
            return (pos, neg)
        pos = ((str((-1*b)/(2*a))+"+"+("i"+"sqrt("+str(discriminant)+")/"+str(2*a))))
        neg = str((-1*b)/(2*a))+"-"+("i"+"sqrt("+str(discriminant)+")/"+str(2*a))
        return (pos, neg)
    pos = ((-1*b)+(discriminant))/(2*a)
    neg = ((-1*b)-discriminant)/(2*a)
    return (((-1*b)+(discriminant))/(2*a), ((-1*b)-discriminant)/(2*a))
a= input("A: ")
b = input("B: ")
c = input("C: ")
print("\n")
print(solver(float(a), float(b), float(c)))