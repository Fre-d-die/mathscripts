import math
a=int(input("what is the coefficient of x^2?"))
b=int(input("what is the coefficeint of x?"))
c=int(input("what is the last number?"))
sqrtThis=(b*b)-(4*a)*(c)
sqrtDone=math.sqrt(sqrtThis)
bAdd=b+sqrtDone
bMinus=b-sqrtDone
answrAdd=str(bAdd/(a*2))
answrMinus=str(bMinus/(a*2))
print("x="+answrMinus)
print("x="+answrAdd)
