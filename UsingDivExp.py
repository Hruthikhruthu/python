def DivExp(a,b):
    assert a>0,"Asserstion Error :a must be greater then 0"
    if b==0:
        raise ZeroDivisionError("Error:division by zero")
    c=a/b
    return c
a=float(input("Enter the value of a:"))
b=float(input("Enter the value of b:"))
try:
    result=DivExp(a,b)
    print("The result of division is:",result)
except(AssertionError,ZeroDivisionError)as e:
    print(e)
    
