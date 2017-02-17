import math
a=int(input("what is the coefficient of x^2?"))
b=int(input("what is the coefficeint of x?"))
c=int(input("what is the last number?"))
answrAdd=str((b+(math.sqrt((b**2)-(4*a)*(c))))/(2*a))
answrMinus=str(str((b-(math.sqrt((b**2)-(4*a)*(c))))/(2*a)))
print("x="+answrAdd)
print("x="+answrMinus)
