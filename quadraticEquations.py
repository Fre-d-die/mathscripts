import math
a = int(input("what is the coefficient of x^2?"))
b = int(input("what is the coefficeint of x?"))
c = int(input("what is the last number?"))
sqrtThis = ((b**2)-(4*a)*(c))/(2*a)
if sqrtThis < 0:
    print("the answer is not a real number")
else:
    sqrt = math.sqrt(((b**2)-(4*a)*(c))/(2*a))
    pstv = str(b+sqrt)
    ngtv = str(b-sqrt)
    print("x=", pstv)
    print("x=", ngtv)
